# Multi-AZ DB Cluster RDS Using CFN

https://awstut.com/en/2023/01/14/multi-az-db-cluster-rds-using-cfn-en/

# Architecture

![fa-112-diagram](https://user-images.githubusercontent.com/84276199/212431600-8d37c307-e72c-4bb0-8321-881c0b638fa1.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-112.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-112/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-112 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-112/fa-112.yaml \
--capabilities CAPABILITY_IAM
```
