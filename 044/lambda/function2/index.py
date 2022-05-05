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

PUT = 'Put'
LIST = 'List'
DELETE = 'Delete'


def lambda_handler(event, context):
  field = ''
  document = None
  result = None
  
  if not 'queryStringParameters' in event or (
      not 'field' in event['queryStringParameters']):
    field = LIST
  else:
    field = event['queryStringParameters']['field']
    
  if field == PUT:
    document = gql(
      """
      mutation PutS3ObjectMutation {
        putS3Object {
          Key
          LastModified
          Size
          ETag
        }
      }
      """
      )
    result = client.execute(document)
  
  elif field == LIST:
    document = gql(
      """
      query ListS3ObjectsQuery {
        listS3Objects {
          Key
        }
      }
      """
      )
    result = client.execute(document)
    
  elif field == DELETE:
    object_name = event['queryStringParameters']['object_name']
    document = gql(
      """
      mutation DeleteS3ObjectsMutation($object_name: String!) {
        deleteS3Object(Key: $object_name) {
          Key
        }
      }
      """
      )
      
    params = {
      'object_name': object_name
    }
    result = client.execute(document, variable_values=params)
  
  return {
    'statusCode': 200,
    'body': json.dumps(result, indent=2)
  }
