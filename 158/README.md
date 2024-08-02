# Create AWS IoT rules and republish MQTT messages

https://awstut.com/en/2024/08/03/create-aws-iot-rules-and-republish-mqtt-messages-en/

# Architecture

![fa-158-diagram](https://github.com/user-attachments/assets/189d7702-32a2-48c2-adf6-d287c9be390a)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-158.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-158/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-158 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-158/fa-158.yaml \
--capabilities CAPABILITY_IAM
```
