import json
import os
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

query = gql(
  """
  query GetDatetimeQuery($id_: ID!) {
    getDatetime(id: $id_) {
      id
      datetime
      epoch
    }
  }
""")

def lambda_handler(event, context):
  if not 'queryStringParameters' in event or (
      not 'id' in event['queryStringParameters']):
    return {
      'statusCode': 200,
      'body': 'No ID.'
    }
    
  id_ = event['queryStringParameters']['id']
  
  params = {
    'id_': id_
  }
    
  result = client.execute(query, variable_values=params)
  
  return {
    'statusCode': 200,
    'body': json.dumps(result, indent=2)
  }
