#import datetime
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


def lambda_handler(event, context):
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
