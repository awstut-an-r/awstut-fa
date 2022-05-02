import datetime
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

mutation = gql(
  """
  mutation AddDatetimeMutation($adddatetimeinput: AddDatetimeInput!) {
    addDatetime(input: $adddatetimeinput) {
      id
      datetime
      epoch
    }
  }
""")

def lambda_handler(event, context):
  now = datetime.datetime.now()
  now_str = now.strftime('%Y%m%d%H%M%S%f')
  epoch_time = int(time.mktime(now.timetuple()))
  
  params = {
    'adddatetimeinput': {
      'datetime': now_str,
      'epoch': epoch_time
    }
  }
    
  result = client.execute(mutation, variable_values=params)
  #print(result)
  
  return {
    'statusCode': 200,
    'body': json.dumps(result, indent=2)
  }