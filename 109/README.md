# Create S3 bucket with versioning enabled with CFN

https://awstut.com/en/2023/01/04/create-s3-bucket-with-versioning-enabled-with-cfn-en/

# Architecture

![fa-109-diagram](https://user-images.githubusercontent.com/84276199/210449556-e20a5f61-71b0-4222-bab4-97fbe9c2431d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-109.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-109/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-109 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-109/fa-109.yaml \
--capabilities CAPABILITY_IAM
```
