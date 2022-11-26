# Connect Aurora Serverless from EC2/Lambda using Data API

https://awstut.com/en/2022/07/09/connect-aurora-serverless-from-ec2-lambda-using-data-api-en/

# Architecture

![fa-059-diagram](https://user-images.githubusercontent.com/84276199/204084768-5aa59d6b-e0f8-4f79-ba15-aeb5ee7e609d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-059.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-059/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-059 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-059/fa-059.yaml \
--capabilities CAPABILITY_IAM
```
