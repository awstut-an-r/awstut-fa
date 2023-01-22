# 4 destinations for S3 event notifications – SNS/SQS/Lambda/EventBridge

https://awstut.com/en/2023/01/22/4-destinations-for-s3-event-notifications-sns-sqs-lambda-eventbridge-en/

# Architecture

![fa-113-diagram](https://user-images.githubusercontent.com/84276199/213899834-92111983-d72f-4c23-8516-0f389be3f206.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-113.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-113/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-113 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-113/fa-113.yaml \
--capabilities CAPABILITY_IAM
```
