# Two Authentication Methods for RDS Proxy – Password / IAM

https://awstut.com/en/2022/04/30/two-authentication-methods-for-rds-proxy-password-and-iam-en/

# Architecture

![fa-039-diagram-01](https://user-images.githubusercontent.com/84276199/200169522-ec73557b-85c1-453c-be60-05adf467e979.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-039.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Create Lambda Layer Package

```bash
pip3 install mysql-connector-python -t ./python

zip -r layer.zip python

aws s3 cp layer.zip s3://fa-039/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-039/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-039 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-039/fa-039.yaml \
--capabilities CAPABILITY_IAM
```
