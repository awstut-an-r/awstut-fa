# Introduction to SQS Data Linkage between Lambdas

https://awstut.com/en/2022/02/05/introduction-to-sqs-data-linkage-between-lambdas-2/

# Architecture

![fa-021-diagram](https://user-images.githubusercontent.com/84276199/191960392-c05af5f6-97e2-4713-9575-c9321c419a8f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-021.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-021/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-021 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-021/fa-021.yaml \
--capabilities CAPABILITY_IAM
```
