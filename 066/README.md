# Subscription filter to extract errors in Fargate container logs and notify by email

https://awstut.com/en/2022/07/31/subscription-filter-to-extract-errors-in-fargate-container-logs-and-notify-by-email-en/

# Architecture

![fa-066-diagram](https://user-images.githubusercontent.com/84276199/204088458-5cb380f1-322e-469b-b27c-ee1ae3a183fb.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-066.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-066/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-066 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-066/fa-066.yaml \
--capabilities CAPABILITY_IAM
```
