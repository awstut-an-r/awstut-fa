# Introduction to AWS Service Catalog using CloudFormation

https://awstut.com/en/2023/04/08/introduction-to-aws-service-catalog-using-cloudformation-en/

# Architecture

![fa-124-diagram](https://user-images.githubusercontent.com/84276199/230685011-bba4aece-a3f7-4d0e-bdb6-65a091c5e914.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-124.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-124/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-124 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-124/fa-124.yaml \
--capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```
