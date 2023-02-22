# Introduction to Creating SSM Automation Runbooks Using CloudFormation

https://awstut.com/en/2023/02/23/introduction-to-creating-ssm-automation-runbooks-using-cloudformation-en/

# Architecture

![fa-119-diagram](https://user-images.githubusercontent.com/84276199/220773013-5530ba1a-b136-4285-9155-840ed56ed5ff.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-119.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-119/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-119 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-119/fa-119.yaml \
--capabilities CAPABILITY_IAM
```
