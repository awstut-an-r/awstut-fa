# Introduction to EC2 Auto Scaling – No Scaling Policy

https://awstut.com/en/2022/10/08/introduction-to-ec2-auto-scaling-no-scaling-policy-en/

# Architecture

![fa-089-diagram](https://user-images.githubusercontent.com/84276199/204132016-6218b183-b1bc-423d-a754-89c5270e9c34.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-089.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-089/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-089 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-089/fa-089.yaml \
--capabilities CAPABILITY_IAM
```
