import boto3
import datetime
import json
import mysql.connector
import os


db_endpoint_port = int(os.environ['DB_ENDPOINT_PORT'])
db_name = os.environ['DB_NAME']
#db_password = os.environ['DB_PASSWORD']
db_proxy_endpoint_address = os.environ['DB_PROXY_ENDPOINT_ADDRESS']
db_tablename = os.environ['DB_TABLENAME']
db_user = os.environ['DB_USER']
region = os.environ['REGION']
ssl_certificate = os.environ['SSLCERTIFICATE']

os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

client = boto3.client('rds', region_name=region)


def lambda_handler(event, context):
    token = client.generate_db_auth_token(
        DBHostname=db_proxy_endpoint_address,
        Port=db_endpoint_port,
        DBUsername=db_user,
        Region=region)
  
    conn = mysql.connector.connect(
        host=db_proxy_endpoint_address,
        user=db_user,
        password=token,
        port=db_endpoint_port,
        database=db_name,
        ssl_ca=ssl_certificate)
    
    cur = conn.cursor()
    
    table_sql = 'create table if not exists {db}.{tbl} (dt datetime);'.format(
        db=db_name,
        tbl=db_tablename
        )
    cur.execute(table_sql)
    
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    write_sql = 'insert into {tbl} values ("{now}");'.format(
        tbl=db_tablename,
        now=now_str
    )
    cur.execute(write_sql)
    
    cur.close()
    conn.commit()
    
    cur = conn.cursor()
    read_sql = 'select * from {tbl};'.format(tbl=db_tablename)
    cur.execute(read_sql)
    content = [record[0].strftime('%Y-%m-%d %H:%M:%S') for record in cur]
    
    cur.close()
    conn.close()
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(content, indent=2)
    }
