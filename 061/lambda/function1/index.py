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

CREATE_PET = 'createPet'
UPDATE_PET = 'updatePet'
DELETE_PET = 'deletePet'
GET_PET = 'getPet'
LIST_PETS = 'listPets'
LIST_PETS_BY_PRICE_RANGE = 'listPetsByPriceRange'


def lambda_handler(event, context):
  operation = ''
  document = None
  result = None
  
  if not 'queryStringParameters' in event or (
      not 'operation' in event['queryStringParameters']):
    operation = LIST_PETS
  else:
    operation = event['queryStringParameters']['operation']
    
  if operation == CREATE_PET:
    document = gql(
      """
      mutation add($type: PetType!, $price: Float!) {
        createPet(input: {
          type: $type,
          price: $price
        }){
          id
          type
          price
        }
      }
      """
      )
      
    params = {
      'type': event['queryStringParameters']['type'],
      'price': event['queryStringParameters']['price']
    }
    
    result = client.execute(document, variable_values=params)
    
  elif operation == UPDATE_PET:
    document = gql(
      """
      mutation update($id: ID!, $type: PetType!, $price: Float!) {
        updatePet(input: {
          id: $id,
          type: $type,
          price: $price
        }){
          id
          type
          price
        }
      }
      """
      )
      
    params = {
      'id': event['queryStringParameters']['id'],
      'type': event['queryStringParameters']['type'],
      'price': event['queryStringParameters']['price']
    }
    
    result = client.execute(document, variable_values=params)
    
  elif operation == DELETE_PET:
    document = gql(
      """
      mutation delete($id: ID!) {
        deletePet(input: {
          id: $id
        }){
          id
          type
          price
        }
      }
      """
      )
      
    params = {
      'id': event['queryStringParameters']['id']
    }
    
    result = client.execute(document, variable_values=params)
    
  elif operation == GET_PET:
    document = gql(
      """
      query get($id: ID!) {
        getPet(id: $id){
          id
          type
          price
        }
      }
      """
      )
      
    params = {
      'id': event['queryStringParameters']['id']
    }
    
    result = client.execute(document, variable_values=params)
    
  elif operation == LIST_PETS:
    document = gql(
      """
      query allpets {
        listPets {
          id
          type
          price
        }
      }
      """
      )
      
    result = client.execute(document)
    
  elif operation == LIST_PETS_BY_PRICE_RANGE:
    document = gql(
      """
      query list($min: Float!, $max: Float!) {
        listPetsByPriceRange(min: $min, max: $max) {
          id
          type
          price
        }
      }
      """
      )
      
    params = {
      'min': event['queryStringParameters']['min'],
      'max': event['queryStringParameters']['max']
    }
    
    result = client.execute(document, variable_values=params)
    
    
  return {
    'statusCode': 200,
    'body': json.dumps(result, indent=2)
  }