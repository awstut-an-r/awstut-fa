# Aurora Serverless v2 creation using CloudFormation

https://awstut.com/en/2023/08/05/aurora-serverless-v2-creation-using-cloudformation-en/

# Architecture

![fa-138-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/586a517f-50b9-416e-8e6d-38537ed26644)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-138.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-138/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-138 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-138/fa-138.yaml \
--capabilities CAPABILITY_IAM
```
