# Enable DynamoDB expiration time (TTL) using CFN

https://awstut.com/en/2022/12/31/enable-dynamodb-expiration-time-ttl-using-cfn-en/

# Architecture

![fa-107-diagram](https://user-images.githubusercontent.com/84276199/210116903-90d4fff5-15b1-4758-9e74-6ed99eed6dd1.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-107.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-107/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-107 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-107/fa-107.yaml \
--capabilities CAPABILITY_IAM
```
