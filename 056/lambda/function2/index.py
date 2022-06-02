import boto3
import cfnresponse
import json
import os
import requests
from requests.auth import HTTPBasicAuth
from requests_aws4auth import AWS4Auth

#PATH = './bulk_movies.json'
BULK_ENDPOINT = os.environ['BULK_ENDPOINT']
#BULK_FILE = os.environ['BULK_FILE']
BULK_S3_BUCKET = os.environ['BULK_S3_BUCKET']
BULK_S3_KEY = os.environ['BULK_S3_KEY']

#MASTER_USERNAME = os.environ['MASTER_USERNAME']
#MASTER_PASSWORD = os.environ['MASTER_PASSWORD']

REGION = os.environ['REGION']

CREATE = 'Create'
response_data = {}

s3_client = boto3.client('s3')

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(
  #credentials.access_key,
  #credentials.secret_key,
  region=REGION,
  service='es',
  refreshable_credentials=credentials
  )


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
        #auth=HTTPBasicAuth(MASTER_USERNAME, MASTER_PASSWORD),
        auth=awsauth,
        headers={'Content-Type': 'application/json'}
        )
      print(requests_response.text)
      
      #with open(BULK_FILE) as f:
      #  bulk = f.read()
      #  #print(s)
      #  #print(requests.get('https://www.google.com/?hl=ja'))
      #  
      #  response = requests.post(
      #    BULK_ENDPOINT,
      #    #headers={
      #    #  'Content-Type': 'application/json'
      #    #},
      #    json=bulk,
      #    auth=HTTPBasicAuth(MASTER_USERNAME, MASTER_PASSWORD)
      #    )
      
    cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data)
        
  except Exception as e:
    print(e)
    cfnresponse.send(event, context, cfnresponse.FAILED, response_data)