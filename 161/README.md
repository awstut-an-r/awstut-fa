# How to Save MQTT Messages to DynamoDB Using AWS IoT Rules

https://awstut.com/en/2024/10/14/how-to-save-mqtt-messages-to-dynamodb-using-aws-iot-rules-en/

# Architecture

![fa-161-diagram](https://github.com/user-attachments/assets/944fc46c-4a26-4a07-a033-30ed733b8d1f)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-161.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-161/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-161 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-161/fa-161.yaml \
--capabilities CAPABILITY_IAM
