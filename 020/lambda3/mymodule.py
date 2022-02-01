import boto3
import os

def get_ssm_parameter(parameter_name, client=None):
  if not client:
    client = boto3.client('ssm', region_name=os.environ['region_name'])
    
  return client.get_parameter(Name=parameter_name)['Parameter']['Value']