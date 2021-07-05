import sys
import logging
import json
import pymysql
import os

'''
共感ユーザーを追加するためのラムダです。
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
#        'GET': lambda conn, x: db_get(conn, x),
        'POST': lambda conn, x: db_post(conn, x),
#        'PUT': lambda conn, x: db_put(conn, x),
#        'DELETE': lambda conn, x: db_delete(conn, x)
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

# 共感ユーザーの追加
def db_post(conn, x):

    # 簡易的なエラーチェック
    if 'data' not in x['body']:
        return db_error('データ構造が不正です')

    payload = json.loads(x['body']);

    # カードID取得
    cardid = x['pathParameters'].get('cardid') if x['pathParameters'] else None
    # 共感ユーザーのID取得
    empathizerid  = payload['data'].get('empathizerid')

    # 簡易的なエラーチェック
    if str.strip(empathizerid) == '':
        return db_error('共感ユーザーIDが空欄です')

    return insert_like(conn, cardid, empathizerid)

def insert_like(conn, cardid, empathizerid):
    with conn.cursor() as cur:
        sql = "insert into Ene_Empathy (id, empathyuser) VALUES (%s, %s)"
        r = cur.execute(sql, (cardid, empathizerid))

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


