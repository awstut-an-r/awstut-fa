# Introduction to AWS IoT Core using CloudFormation

https://awstut.com/en/2024/03/02/introduction-to-aws-iot-core-using-cloudformation-en/

# Architecture

![fa-151-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/a2d605a3-0b41-4722-aa95-09e73a94f3e6)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-151.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-151/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-151 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-151/fa-151.yaml \
--capabilities CAPABILITY_IAM
```
