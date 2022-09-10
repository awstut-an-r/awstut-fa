# Create sign-in page in Cognito user pool

https://awstut.com/en/2021/12/12/create-a-sign-in-page-in-the-cognito-user-pool/

# Architecture

![fa-010-diagram](https://user-images.githubusercontent.com/84276199/189460455-f0040f06-9575-4300-bc89-13335d5709f6.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-010.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-010/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-010 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-010/fa-010.yaml \
--capabilities CAPABILITY_IAM
```

## Upload HTML files

```bash
aws s3 cp ./html s3://fa-010/ --recursive
```
