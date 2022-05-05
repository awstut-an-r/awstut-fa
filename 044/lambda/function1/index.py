import boto3
import json
import os
from datetime import date, datetime

bucket_name = os.environ['BUCKET_NAME']
s3_client = boto3.client('s3')

PUT = 'Put'
LIST = 'List'
DELETE = 'Delete'

def json_serial(obj):
  # reference: https://www.yoheim.net/blog.php?q=20170703
  if isinstance(obj, (datetime, date)):
    return obj.isoformat()
  raise TypeError ("Type %s not serializable" % type(obj))

def lambda_handler(event, context):
  if event['field'] == PUT:
    now = datetime.now()
    now_str = now.strftime('%Y%m%d%H%M%S')
    
    key = "{datetime}.txt".format(datetime=now_str)
    
    put_response = s3_client.put_object(
      Bucket=bucket_name,
      Key=key,
      Body=now_str.encode())
    #print(put_response)
      
    get_response = s3_client.get_object(
      Bucket=bucket_name,
      Key=key)
    #print(get_response)
      
    object_ = {
      'Key': key,
      'LastModified': get_response['LastModified'],
      'Size': get_response['ContentLength'],
      #'StorageClass': get_response['StorageClass'],
      'ETtag': get_response['ETag']
    }
    #return json.dumps(objects)
    return json.dumps(object_, default=json_serial)
  
  elif event['field'] == LIST:
    list_response = s3_client.list_objects_v2(
      Bucket=bucket_name)
      
    objects = list_response['Contents']
    #objects = [
    #  {
    #    'key': 'hogehoge.txt',
    #    'lastModified': '2022-05-04 10:00',
    #    'size': 100,
    #    'storageClass': 'STANDARD',
    #    'etag': '1234567890abc'
    #  }
    #]
    
    #return json.dumps(objects)
    return json.dumps(objects, default=json_serial)
    
  elif event['field'] == DELETE:
    #print(event['arguments'])
    key = event['arguments']['Key']
    
    delete_response = s3_client.delete_object(
      Bucket=bucket_name,
      Key=key)
    #print(delete_response)
      
    object_ = {
      'Key': key
    }
    return json.dumps(object_, default=json_serial)
    
  #else:
  #  return None