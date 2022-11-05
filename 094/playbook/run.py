import datetime
import json
import mysql.connector
import os
from flask import Flask

db_name = os.environ['DB_NAME']
db_password = os.environ['DB_PASSWORD']
db_read_endpoint_address = os.environ['DB_READ_ENDPOINT_ADDRESS']
db_tablename = os.environ['DB_TABLENAME']
db_user = os.environ['DB_USER']
db_write_endpoint_address = os.environ['DB_WRITE_ENDPOINT_ADDRESS']
mysql_port = int(os.environ['MYSQL_PORT'])

str_format = '%Y-%m-%d %H:%M:%S'

app = Flask(__name__)

@app.route('/')
@app.route('/read')
def read():
  conn = mysql.connector.connect(
    host=db_read_endpoint_address,
    port=mysql_port,
    user=db_user,
    password=db_password,
    database=db_name
    )
  cur = conn.cursor()
  
  read_sql = 'select * from {table};'.format(table=db_tablename)
  cur.execute(read_sql)
  result = json.dumps(
    [record[0].strftime(str_format) for record in cur],
    indent=2
    )
  
  cur.close()
  conn.close()
  
  return result
  

@app.route('/write')
def write():
  conn = mysql.connector.connect(
    host=db_write_endpoint_address,
    port=mysql_port,
    user=db_user,
    password=db_password,
    database=db_name
    )
  cur = conn.cursor()
  
  now = datetime.datetime.now()
  now_str = now.strftime(str_format)
  write_sql = 'insert into {table} values ("{now}");'.format(
    table=db_tablename,
    now=now_str
    )
  cur.execute(write_sql)
  
  cur.close()
  conn.commit()
  conn.close()
  
  return 'Saved: {now}'.format(now=now_str)
  
    
if __name__ == '__main__':
  app.run()
