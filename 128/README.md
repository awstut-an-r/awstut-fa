# Connect to RDS from EC2 (Linux)/Lambda using IAM authentication

https://awstut.com/en/2023/05/06/connect-to-rds-from-ec2-linux-lambda-using-iam-authentication-en/

# Architecture

![fa-128-diagram](https://user-images.githubusercontent.com/84276199/236579106-a8c7976a-b5ea-441f-8201-2bfbb4a33627.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-128.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-128/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-128 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-128/fa-128.yaml \
--capabilities CAPABILITY_IAM
```
