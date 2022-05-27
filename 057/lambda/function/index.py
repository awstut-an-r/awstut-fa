import boto3
import cfnresponse
import json
import os
import requests
from requests.auth import HTTPBasicAuth

BULK_ENDPOINT = os.environ['BULK_ENDPOINT']
BULK_S3_BUCKET = os.environ['BULK_S3_BUCKET']
BULK_S3_KEY = os.environ['BULK_S3_KEY']

MASTER_USERNAME = os.environ['MASTER_USERNAME']
MASTER_PASSWORD = os.environ['MASTER_PASSWORD']

CREATE = 'Create'
response_data = {}

s3_client = boto3.client('s3')

def lambda_handler(event, context):
  try:
    if event['RequestType'] == CREATE:
      s3_response = s3_client.get_object(
        Bucket=BULK_S3_BUCKET,
        Key=BULK_S3_KEY)
        
      # binary
      bulk = s3_response['Body'].read()
      print(bulk)
      
      requests_response = requests.post(
        BULK_ENDPOINT,
        data=bulk,
        auth=HTTPBasicAuth(MASTER_USERNAME, MASTER_PASSWORD),
        headers={'Content-Type': 'application/json'}
        )
      print(requests_response.text)
      
    cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        
  except Exception as e:
    print(e)
    cfnresponse.send(event, context, cfnresponse.FAILED, response_data)
