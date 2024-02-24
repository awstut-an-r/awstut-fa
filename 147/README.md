# Create OpenSearch Serverless using CloudFormation

https://awstut.com/en/2024/02/25/create-opensearch-serverless-using-cloudformation-en/

# Architecture

![fa-147-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/48f43f91-fc42-4a86-8306-b3aafcd2c241)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-147.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-147/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-147 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-147/fa-147.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
