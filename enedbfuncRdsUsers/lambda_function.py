import sys
import logging
import pymysql
import os
import json
import re

'''
ユーザー情報を操作するためのラムダです。
・マイページ用のユーザー情報取得
'''

#rds settings
RDS_HOST = os.environ.get('RDS_HOST')
RDS_USERNAME = os.environ.get('RDS_USERNAME')
RDS_PASSWORD = os.environ.get('RDS_PASSWORD')
RDS_DBNAME = os.environ.get('RDS_DBNAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(RDS_HOST, 
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
    # httpMethodに応じて処理を振り分け
    operations = {
        'GET'   : lambda conn, x: db_get(conn, x),
#        'POST'  : lambda conn, x: db_post(conn, x), 
#        'PUT'   : lambda conn, x: db_post(conn, x),
#        'DELETE': lambda conn, x: db_delete(conn, x),
    }
    
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
ユーザー情報取得
 クエリパラメータ
 id=取得するID
 省略時は全データ
 戻り値（JSON）
 {
   result : 1（成功） もしくは 0（失敗）
   error : エラーのときのメッセージ配列
   data : {
     userid : ユーザーID
     department : 所属部署
     imageurl : プロフィール画像URL
     name : 名前
     profile : プロフィール文
   }
 } 
'''
def db_get(conn, x):
    print(json.dumps(x))
    
    # パラメータに取得するIDが設定されている場合
    id = x['pathParameters'].get('userid') if x['pathParameters'] else None
    if id is not None and re.match(r"^\d+$", str(id)):

        # 該当idのものをクエリー
        with conn.cursor() as cur:
            sql = "select * from Ene_Users WHERE userid = %s"
            cur.execute(sql, (id))
            
            # ユーザー情報がない場合、エラーを返す
            if cur.rowcount == 0:
                return db_error('ユーザー情報がありません')
            
            # 戻り値を設定して返す
            result = cur.fetchall()
            
        return {
            'result' : 1,
            'error' : '',
            'data' : result
        }
    
    # パラメータ省略時は全データ取得
    else:
        with conn.cursor() as cur:
            cur.execute("select * from Ene_Users")
            
            # 戻り値を設定して返す
            result = cur.fetchall()
    
        return {
            'result' : 1,
            'error' : '',
            'data' : result
        }
            

# レスポンス
def respond(res):
    print(json.dumps(res))
    return {
        'statusCode': '400' if res['error'] else '200',
        'body': str(res['error']) if res['error'] else json.dumps(res).encode(),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin' : '*'
        },
    }


# エラー用
def db_error(msg):
    return {
        'result' : 0,
        'error' : msg,
        'data' : {}
    } 