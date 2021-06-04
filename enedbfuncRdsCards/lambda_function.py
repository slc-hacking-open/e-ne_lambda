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


# eねカード取得
def db_get(conn, x):

    # カードID取得
    cardid = x['pathParameters'].get('cardid') if x['pathParameters'] else None
    # 送信者ID取得
    senderId = x['queryStringParameters'].get('senderId') if x['queryStringParameters'] else None
    # 受信者ID取得
    receiverId = x['queryStringParameters'].get('receiverId') if x['queryStringParameters'] else None

    with conn.cursor() as cur:
        # パラメータにカードIDが設定されている場合
        if cardid is not None and re.match(r"^\d+$", str(cardid)):
            sql = "select * from Ene_Messages WHERE id = %s"
            cur.execute(sql, (cardid))
            result = cur.fetchall()
            if cur.rowcount == 0:
                return db_error('eねがありません')
        else:
            # パラメータに送信者IDが設定されている場合
            if senderId is not None and re.match(r"^\d+$", str(senderId)):
                sql = "select * from Ene_Messages WHERE sender = %s order by datetime desc limit 100"
                cur.execute(sql, (senderId))
                result = cur.fetchall()
            # パラメータに受信者IDが設定されている場合
            elif senderId is not None and re.match(r"^\d+$", str(receiverId)):
                sql = "select * from Ene_Messages WHERE receiver = %s order by datetime desc limit 100"
                cur.execute(sql, (receiverId))
                result = cur.fetchall()
            else:
                cur.execute("select * from Ene_Messages order by datetime desc limit 100")
                result = cur.fetchall()

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
            results = []
            for k,v in d.items():
                if k == 'sender' or k == 'receiver':
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
                            sql = "select * from Ene_Users WHERE userid = %s"
                            cur.execute(sql, (v))
                            result = cur.fetchall()
                            results.append(result[0])
                    data['empathyUsers'] = results
                else:
                    data[k] = v

            datalist.append(data)

    return datalist


# eね投稿
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
        receiver   = x['data'].get('receiverid')
        sender     = x['data'].get('senderid')
#        amount     = x['data'].get('amount')

        # 簡易的なエラーチェック
        if str.strip(contents) == '':
            return db_error('いいね内容が空欄です')
        if not re.match(r"^\d+$", str(receiver)):
            return db_error('送り先IDが正しくありません')
        if not re.match(r"^\d+$", str(sender)):
            return db_error('送り主IDが正しくありません')
#        if str.strip(amount) == '':
#            return db_error('送信コインが空欄です')

        # システム日付取得
        sysdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        # DBに書き込む
        with conn.cursor() as cur:
            sql = "insert into Ene_Messages (contents, sender, receiver, datetime) VALUES (%s, %s, %s, %s)"
            r = cur.execute(sql, (contents, sender, receiver, sysdate))
            print(r)
            sql = "select * from Ene_Messages WHERE id = %s"
            insertid = conn.insert_id()
            cur.execute(sql, (insertid))
            result = cur.fetchall()
            conn.commit()

        # ユーザー情報の取得
        # sender、receiverのidに紐づくユーザー情報を取得
        with conn.cursor() as cur:
            sql = "select * from Ene_Users WHERE userid = %s"
            cur.execute(sql, (sender))
            senderresult = cur.fetchall()
            cur.execute(sql, (receiver))
            receiverresult = cur.fetchall()

        item = {
                'id' : insertid,
                'contents' : contents,
                'receiver' : receiverresult[0],
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

# eね削除
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


