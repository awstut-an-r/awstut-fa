#import boto3
import json
import os
import mymodule

def lambda_handler(event, context):
  ssm_parameter_name = os.environ['ssm_parameter_name']
  ssm_parameter = mymodule.get_ssm_parameter(ssm_parameter_name)

  return {
    'statusCode': 200,
    'body': json.dumps(ssm_parameter)
  }
