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
        'PUT': lambda conn, x: db_put(conn, x),
        'DELETE': lambda conn, x: db_delete(conn, x)
    }
    
    print(event);

    operation = event['httpMethod']
    if operation in operations:
        if operation == 'GET':
            payload = event['queryStringParameters']
        else:
            payload = json.loads(event['body']);
        
        return respond(operations[operation](conn, payload))
        
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
# クエリパラメータ
# userid: ログインユーザーID（共感情報取得のため）
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
#            "hasEmpathized": 共感しているかどうか
#            "empathyCount": 共感数
#        }
#   ]
# }
'''
def db_get(conn, x):
    
    userid = str(x.get('userid'))
    
    with conn.cursor() as cur:
        cur.execute("select * from Ene_Messages order by datetime desc limit 100")
            
        # 戻り値を設定して返す
        result = cur.fetchall()
    
    if cur.rowcount == 0:
        return db_error('eねがありません')
        
    # ユーザー情報の取得
    # sender、recieverのidに紐づくユーザー情報を取得
    datalist = []
    with conn.cursor() as cur:
        for d in result:
            data = {}
            for k,v in d.items():
                if k == 'sender' or k == 'reciever':
                    sql = "select * from Ene_Users WHERE userid = %s"
                    cur.execute(sql, (v))
                    result = cur.fetchall()
                    data[k] = result
                elif k == 'id':
                    sql = "select * from Ene_Empathy WHERE id = %s and empathyuser = %s"
                    cur.execute(sql, (v, userid))
                    result = cur.fetchall()
                    
                    if cur.rowcount != 0 :
                        data['hasEmpathized'] = True
                    else:
                        data['hasEmpathized'] = False
                    
                    sql = "select count(*) from Ene_Empathy WHERE id = %s"
                    cur.execute(sql, (v))
                    result = cur.fetchall()
                    
                    data['empathyCount'] = result[0].values()
                
                    data[k] = v
                else:
                    data[k] = v
        
            datalist.append(data)
                
    return {
        'result' : 1,
        'error' : '',
        'data' : datalist
    }


# eね投稿
#
# {
#   body: {
#     data: {
#       sender: 送り主ユーザーID
#       reciever: 送り先ユーザーID
#       contents: 内容
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
    
    print(x)
    
    # 簡易的なエラーチェック
    if 'data' not in x:
        return db_error('データ構造が不正です')

    contents   = x['data'].get('contents')
    reciever   = x['data'].get('reciever')
    sender     = x['data'].get('sender')
    
    # 簡易的なエラーチェック
    if str.strip(contents) == '':
        return db_error('いいね内容が空欄です')
    if not re.match(r"^\d+$", str(reciever)):
        return db_error('送り先IDが正しくありません')
    if not re.match(r"^\d+$", str(sender)):
        return db_error('送り主IDが正しくありません')
    
    # システム日付取得
    sysdate = str(datetime.datetime.now())
    
    # DBに書き込む
    with conn.cursor() as cur:
        sql = "insert into Ene_Messages (contents, sender, reciever, datetime) VALUES (%s, %s, %s, %s)"
        r = cur.execute(sql, (contents, sender, reciever, sysdate))
        print(r)
        sql = "select * from Ene_Messages WHERE id = %s"
        cur.execute(sql, (conn.insert_id()))
        result = cur.fetchall()
        conn.commit()
    
    return {
        'result' : 1,
        'error' : '',
        'data' : result
    }
 
'''  
# 共感数更新
#
# {
#   body: {
#     data: {
#       id: eねカードID
#       userid: 共感したユーザーのID
#     }
#   }
# }
#
# 戻り値（JSON）
# {
#   result : 1（成功） もしくは 0（失敗）
#   error : エラーのときのメッセージ配列
#   data : { 
#     更新数
#   }
'''
def db_put(dynamo, x):
    
    print(x)
    
    id = x['data'].get('id')
    empathyuser = x['data'].get('userid')
    
    with conn.cursor() as cur:
        sql = "select * from Ene_Empathy WHERE id = %s and empathyuser = %s"
        cur.execute(sql, (id, empathyuser))
        result = cur.fetchall()
                    
        if cur.rowcount == 0 :
            sql = "insert into Ene_Empathy (id, empathyuser) VALUES (%s, %s)"
            r = cur.execute(sql, (id, empathyuser))
            print("insert")
        
        else:
            sql = "delete from Ene_Empathy where id = %s and empathyuser = %s"
            r = cur.execute(sql, (id, empathyuser))
            print("delete")
        
        conn.commit()
    
    return {
        'result' : 1,
        'error' : '',
        'data' : r
    }
                
def respond(res):
    return {
        'statusCode': '400' if res['error'] else '200',
        'body': str(res['error']) if res['error'] else json.dumps(res, default=date_handler),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin' : '*'
        },
    }
    
def db_delete(conn, x):
    return {
        
    }

def db_error(msg):
    return {
        'result' : 0,
        'error' : msg,
        'data' : {}
    }
    
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj
