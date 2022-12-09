# Invoking Lambda from SNS

https://awstut.com/en/2022/12/10/invoking-lambda-from-sns-en/

# Architecture

![fa-100-diagram](https://user-images.githubusercontent.com/84276199/206803132-2472e529-d40f-46c0-8063-38a414867435.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-100.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-100/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-100 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-100/fa-100.yaml \
--capabilities CAPABILITY_IAM
```
