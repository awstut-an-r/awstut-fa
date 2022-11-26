# Introduction to SNS with CFN – email version

https://awstut.com/en/2022/07/30/introduction-to-sns-with-cfn-email-en/

# Architecture

![fa-067-diagram](https://user-images.githubusercontent.com/84276199/204088638-89bf21b0-4ff2-43a7-93e7-f7c87bfab9c0.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-067.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-067/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-067 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-067/fa-067.yaml \
--capabilities CAPABILITY_IAM
```
