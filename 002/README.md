# Yum on private subnet instances

https://awstut.com/en/2021/12/11/run-yum-on-a-private-subnet-instance/

# Architecture

![fa-002-diagram](https://user-images.githubusercontent.com/84276199/188271580-46529129-534f-437a-b36c-0bb905c99d7c.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-002.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-002/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-002 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-002/fa-002.yaml \
--capabilities CAPABILITY_IAM
```
