# Create AMI using SSM Automation (one-time/scheduled)

https://awstut.com/en/2023/02/19/create-ami-using-ssm-automation-one-time-scheduled-en/

# Architecture

![fa-118-diagram](https://user-images.githubusercontent.com/84276199/219937421-09209a89-8068-473d-a2fb-de6be72cd12f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-118.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-118/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-118 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-118/fa-118.yaml \
--capabilities CAPABILITY_IAM
```
