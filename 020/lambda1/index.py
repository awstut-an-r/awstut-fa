#import boto3
import json
import os
import mymodule

def lambda_handler(event, context):
  ssm_parameter_name = os.environ['ssm_parameter_name']
  #region_name = os.environ['region_name']
  #
  #ssm = boto3.client('ssm', region_name=region_name)
  #ssm_parameter = ssm.get_parameter(
  #  Name=ssm_parameter_name)['Parameter']['Value']
  ssm_parameter = mymodule.get_ssm_parameter(ssm_parameter_name)

  return {
    'statusCode': 200,
    'body': json.dumps(ssm_parameter)
  }