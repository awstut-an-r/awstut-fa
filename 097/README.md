# Introduction to AWS Config with CFN – Auditing S3 Bucket Logging Settings

https://awstut.com/en/2022/12/03/introduction-to-aws-config-with-cfn-auditing-s3-bucket-logging-settings-en/

# Architecture

![fa-097-diagram](https://user-images.githubusercontent.com/84276199/205404205-bbfcec79-cb4a-407a-ac15-770d95e523fd.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-097.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-097/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-097 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-097/fa-097.yaml \
--capabilities CAPABILITY_IAM
```
