# Notifying SNS using AWS IoT rules

https://awstut.com/en/2024/08/31/notifying-sns-using-aws-iot-rules-en/

# Architecture

![fa-160-diagram](https://github.com/user-attachments/assets/4aca0a54-0fa2-4022-b363-d6ddaae9d143)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-160.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-160/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-160 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-160/fa-160.yaml \
--capabilities CAPABILITY_IAM
