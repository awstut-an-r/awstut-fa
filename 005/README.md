# Serverless apps using Lambda and API Gateway – HTTP API

https://awstut.com/en/2021/12/11/serverless-apps-using-lambda-and-api-gateway/

# Architecture

![fa-005-diagram](https://user-images.githubusercontent.com/84276199/188431936-6c90d2a0-0bb3-49c7-abe7-cf83ec95b65e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-005.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-005/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-005 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-005/fa-005.yaml \
--capabilities CAPABILITY_IAM
```
