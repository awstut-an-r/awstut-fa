# AWS IoT rules to execute Lambda functions when receiving MQTT messages

https://awstut.com/en/2024/11/04/aws-iot-rules-to-execute-lambda-functions-when-receiving-mqtt-messages-en/

# Architecture

![fa-162-diagram](https://github.com/user-attachments/assets/cd57d289-845e-4aee-be0f-4763c7fa9631)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-162.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-162/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-162 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-162/fa-162.yaml \
--capabilities CAPABILITY_IAM
