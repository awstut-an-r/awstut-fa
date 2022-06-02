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

LIST = 'List'
GET = 'Get'
ACTOR = 'Actor'
ADD = 'Add'


def lambda_handler(event, context):
  operation = ''
  document = None
  result = None
  
  if not 'queryStringParameters' in event or (
      not 'operation' in event['queryStringParameters']):
    operation = LIST
  else:
    operation = event['queryStringParameters']['operation']
    
  if operation == LIST:
    document = gql(
      """
      query ListMovies {
        listMovies {
          _id
          title
        }
      }
      """
      )
    result = client.execute(document)
    
  elif operation == GET:
    document = gql(
      """
      query GetMovie($_id: ID!) {
        getMovie(_id: $_id) {
          _id
          director
          genre
          year
          actor
          title
        }
      }
      """
      )
    
    _id = event['queryStringParameters']['_id']
    params = {
      '_id': _id
    }
    result = client.execute(document, variable_values=params)
    
  elif operation == ACTOR:
    document = gql(
      """
      query GetMovieByActor($actor: String!) {
        getMovieByActor(actor: $actor) {
          _id
          actor
          title
        }
      }
      """
      )
    
    actor = event['queryStringParameters']['actor']
    params = {
      'actor': actor
    }
    result = client.execute(document, variable_values=params)
    
  elif operation == ADD:
    document = gql(
      """
      mutation AddMovie($director: String, $genre: [String], $year: Int, $actor: [String], $title: String) {
        addMovie(director: $director, genre: $genre, year: $year, actor: $actor, title: $title) {
          _id
          director
          genre
          year
          actor
          title
        }
      }
      """
      )
    
    director = event['queryStringParameters']['director']
    genre = event['queryStringParameters']['genre'].split(',')
    year = int(event['queryStringParameters']['year'])
    actor = event['queryStringParameters']['actor'].split(',')
    title = event['queryStringParameters']['title']
    params = {
      'director': director,
      'genre': genre,
      'year': year,
      'actor': actor,
      'title': title
    }
    result = client.execute(document, variable_values=params)
    
  return {
    'statusCode': 200,
    'body': json.dumps(result, indent=2)
  }
