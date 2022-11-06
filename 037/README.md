# Connect to RDS from Lambda in VPC via RDS Proxy

https://awstut.com/en/2022/04/23/connect-to-rds-from-lambda-in-vpc-via-rds-proxy-en/

# Architecture

![fa-037-diagram](https://user-images.githubusercontent.com/84276199/200168164-d8925ed6-4540-46d4-9494-ef55a33ff4bb.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-037.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Create Lambda Function Package.

```bash
pip3 install mysql-connector-python -t ./lambda

$ zip -r deploy.zip ./lambda
```

## Upload  Template Files and Lambda Function Package to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-037/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-037 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-037/fa-037.yaml \
--capabilities CAPABILITY_IAM
```
