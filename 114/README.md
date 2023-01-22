# Triggering Lambda function from SQS queue

https://awstut.com/en/2023/01/22/triggering-lambda-function-from-sqs-queue-en/

# Architecture

![fa-114-diagram](https://user-images.githubusercontent.com/84276199/213912509-9f557e57-9a7f-4bc0-a4ef-6ea174945d8e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-104.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-104/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-104 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-104/fa-104.yaml \
--capabilities CAPABILITY_IAM
```
