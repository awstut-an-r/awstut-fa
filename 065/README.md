# Deliver Logs of Fargate containers in Private Subnets to CloudWatch Logs

https://awstut.com/en/2022/07/24/deliver-logs-of-fargate-containers-in-private-subnets-to-cloudwatch-logs-en/

# Architecture

![fa-065-diagram](https://user-images.githubusercontent.com/84276199/204087986-93e5c6f5-d4f7-40c2-a214-b32ab9347804.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-065.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-065/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-065 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-065/fa-065.yaml \
--capabilities CAPABILITY_IAM
```
