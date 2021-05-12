import sys
import logging
import json
import pymysql
import re
import os
import datetime

'''
eねを取得・更新するためのラムダです。
'''
#rds settings
RDS_HOST = os.environ.get('RDS_HOST')
RDS_USERNAME = os.environ.get('RDS_USERNAME')
RDS_PASSWORD = os.environ.get('RDS_PASSWORD')
RDS_DBNAME = os.environ.get('RDS_DBNAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=RDS_HOST, 
                           user=RDS_USERNAME, 
                           passwd=RDS_PASSWORD, 
                           db=RDS_DBNAME, 
                           connect_timeout=5,
                           cursorclass=pymysql.cursors.DictCursor)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):

    operations = {
        'GET': lambda conn, x: db_get(conn, x),
        'POST': lambda conn, x: db_post(conn, x),
#        'PUT': lambda conn, x: db_put(conn, x),
        'DELETE': lambda conn, x: db_delete(conn, x)
    }
    
    print(event);

    operation = event['httpMethod']
    if operation in operations:
        return respond(operations[operation](conn, event))
        
    # CORS対応
    elif operation == 'OPTIONS':
        return {
            'statusCode': '200',
            'body': '',
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Methods' : ','.join(operations),
                'Access-Control-Allow-Headers' : 'Origin, Authorization, Accept, Content-Type'
            },
        }

    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))


'''
eねカード取得
#
# パスパラメータ
# cardid: カードID
#
# 戻り値（JSON）
# {
#   result : 1（成功） もしくは 0（失敗）
#   error : エラーのときのメッセージ配列
#   data : [
#       {   
#           "id": eねカードのID
#           "sender":[ 送り主
#                {
#                    "name": 名前
#                    "imageurl" プロフィール画像
#                }
#            ], 
#            "reciever":[ 
#                { 
#                  "name": 名前
#                  "imageurl" プロフィール画像
#                }
#            ],
#            "contents": eね内容
#            "datetime": 更新時間
#            "empathyUserIds"　共感しているユーザー
#        }
#   ]
# }
'''
def db_get(conn, x):
    
    # カードID取得
    cardid = x['pathParameters'].get('cardid') if x['pathParameters'] else None
    
    with conn.cursor() as cur:
        # パラメータにカードIDが設定されている場合
        if cardid is not None and re.match(r"^\d+$", str(cardid)):
            sql = "select * from Ene_Messages WHERE id = %s"
            cur.execute(sql, (cardid))
            result = cur.fetchall()
        
        else:
            cur.execute("select * from Ene_Messages order by datetime desc limit 100")
            result = cur.fetchall()
    
        if cur.rowcount == 0:
            return db_error('eねがありません')
            
    return {
        'result' : 1,
        'error' : '',
        'data' : edit_enecarddata(result)
    }

def edit_enecarddata(dbresult):

    datalist = []
        
    with conn.cursor() as cur:
        for d in dbresult:
            data = {}
            likeUserIds = []
            for k,v in d.items():
                if k == 'sender' or k == 'reciever':
                    sql = "select * from Ene_Users WHERE userid = %s"
                    cur.execute(sql, (v))
                    result = cur.fetchall()
                    data[k] = result[0]
                    
                # 共感している人の情報を取得
                elif k == 'id':
                    data[k] = v
                    sql = "select empathyuser from Ene_Empathy WHERE id = %s"
                    cur.execute(sql, (v))
                    likeUsers = cur.fetchall()
                    for d in likeUsers:
                        for k,v in d.items():
                            likeUserIds.append(v)
                    data['empathyUserIds'] = likeUserIds
                else:
                    data[k] = v
        
            datalist.append(data)
    
    return datalist


# eね投稿
#
# パスパラメータ
# cardid=eねカードID
# 省略時は新規投稿、設定時は共感
#
# {
#   body: {
#     data: {
#       sender: 送り主ユーザーID
#       reciever: 送り先ユーザーID
#       contents: 内容
#       giftCoin: 送信コイン
#       userid: 共感ユーザーID
#     }
#   }
# }
#
# 戻り値（JSON）
# {
#   result : 1（成功） もしくは 0（失敗）
#   error : エラーのときのメッセージ配列
#   data : { 
#     設定されたデータ（形式は入力データと同じ）
#   }
def db_post(conn, x):
    
    # 簡易的なエラーチェック
    if 'data' not in x['body']:
        return db_error('データ構造が不正です')
    
    payload = json.loads(x['body']);
    
    # パラメータにカードIDが設定されている場合、共感数を更新
    cardid = x['pathParameters'].get('cardid') if x['pathParameters'] else None
    if cardid is not None and re.match(r"^\d+$", str(cardid)):

        empathizerid  = payload['data'].get('empathizerid')
    
        # 簡易的なエラーチェック
        if str.strip(empathizerid) == '':
            return db_error('共感ユーザーIDが空欄です')
            
        return insert_like(conn, cardid, empathizerid)
    
    # パラメータ省略時は新規追加
    else:
        return insert_ene(conn, payload)

def insert_like(conn, cardid, empathizerid):
    with conn.cursor() as cur:
        sql = "select * from Ene_Empathy WHERE id = %s and empathyuser = %s"
        cur.execute(sql, (cardid, empathizerid))
        result = cur.fetchall()
                    
        if cur.rowcount == 0 :
            sql = "insert into Ene_Empathy (id, empathyuser) VALUES (%s, %s)"
            r = cur.execute(sql, (cardid, empathizerid))
        
        else:
            sql = "delete from Ene_Empathy where id = %s and empathyuser = %s"
            r = cur.execute(sql, (cardid, empathizerid))
        
        conn.commit()
    
    return {
        'result' : 1,
        'error' : '',
        'data' : r
    }

def insert_ene(conn, x):
        contents   = x['data'].get('contents')
        reciever   = x['data'].get('recieverid')
        sender     = x['data'].get('senderid')
#        amount     = x['data'].get('amount')
    
        # 簡易的なエラーチェック
        if str.strip(contents) == '':
            return db_error('いいね内容が空欄です')
        if not re.match(r"^\d+$", str(reciever)):
            return db_error('送り先IDが正しくありません')
        if not re.match(r"^\d+$", str(sender)):
            return db_error('送り主IDが正しくありません')
#        if str.strip(amount) == '':
#            return db_error('送信コインが空欄です')
    
        # システム日付取得
        sysdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
        # DBに書き込む
        with conn.cursor() as cur:
            sql = "insert into Ene_Messages (contents, sender, reciever, datetime) VALUES (%s, %s, %s, %s)"
            r = cur.execute(sql, (contents, sender, reciever, sysdate))
            print(r)
            sql = "select * from Ene_Messages WHERE id = %s"
            insertid = conn.insert_id()
            cur.execute(sql, (insertid))
            result = cur.fetchall()
            conn.commit()
        
        # ユーザー情報の取得
        # sender、recieverのidに紐づくユーザー情報を取得
        with conn.cursor() as cur:
            sql = "select * from Ene_Users WHERE userid = %s"
            cur.execute(sql, (sender))
            senderresult = cur.fetchall()
            cur.execute(sql, (reciever))
            recieverresult = cur.fetchall()
        
        item = {
                'id' : insertid,
                'contents' : contents,
                'reciever' : recieverresult[0],
                'sender'   : senderresult[0],
                'datetime' : sysdate,
                'empathyUserIds' : []
                }
    
        return {
            'result' : 1,
            'error' : '',
            'data' : item
        } 

# 未使用
def db_put(dynamo, x):
    
    return {
    }

'''  
# eね削除
#
# パスパラメータ
# cardid=eねカードID
#
# {
#   body: {
#     data: {
#       id: eねカードID
#     }
#   }
# }
#
# 戻り値（JSON）
# {
#   result : 1（成功） もしくは 0（失敗）
#   error : エラーのときのメッセージ配列
#   data : { 
#     削除件数
#   }
'''
def db_delete(conn, x):
    
    cardid = x['pathParameters'].get('cardid') if x['pathParameters'] else None
    with conn.cursor() as cur:
        sql = "delete from Ene_Messages WHERE id = %s"
        r = cur.execute(sql, (cardid))
        
        conn.commit()
    
    return {
        'result' : 1,
        'error' : '',
        'data' : r
    }
        
                
def respond(res):
    print(json.dumps(res))
    return {
        'statusCode': '400' if res['error'] else '200',
        'body': str(res['error']) if res['error'] else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin' : '*'
        },
    }

def db_error(msg):
    return {
        'result' : 0,
        'error' : msg,
        'data' : {}
    }
    

