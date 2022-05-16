import json
import os
import time
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

api_key = os.environ['API_KEY']
graphql_url = os.environ['GRAPHQL_URL']

transport = AIOHTTPTransport(
  url=graphql_url,
  headers={
    'x-api-key': api_key
  })
client = Client(transport=transport, fetch_schema_from_transport=True)

ADD = 'Put'
LIST = 'List'


def lambda_handler(event, context):
  field = ''
  document = None
  result = None
  
  if not 'queryStringParameters' in event or (
      not 'operation' in event['queryStringParameters']):
    operation = LIST
  else:
    operation = event['queryStringParameters']['operation']
    
  if operation == ADD:
    key = event['queryStringParameters']['key']
    document = gql(
      """
      mutation AddSampleData($key: String!) {
        addSampleData(key: $key) {
          key
          datetime
        }
      }
      """
      )
    
    params = {
      'key': key
    }
    result = client.execute(document, variable_values=params)
  
  elif operation == LIST:
    document = gql(
      """
      query ListSampleDatas {
        listSampleDatas {
          key
        	datetime
        }
      }
      """
      )
    result = client.execute(document)
    
  return {
    'statusCode': 200,
    'body': json.dumps(result, indent=2)
  }
