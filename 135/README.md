# Introduction to CloudFormation StackSets

https://awstut.com/en/2023/07/08/introduction-to-cloudformation-stacksets-en/

# Architecture

![fa-135-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/a0033aed-f32d-481a-9a8b-21da5d082fe8)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-135.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-135/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-135 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-135/fa-135.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
