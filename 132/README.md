# Restrict access to ALB to via CloudFront

https://awstut.com/en/2023/06/11/restrict-access-to-alb-to-via-cloudfront-en/

# Architecture

![fa-132-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/2fa5b31d-af3c-43e5-8943-87c37cf315e4)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-132.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-132/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-132 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-132/fa-132.yaml \
--capabilities CAPABILITY_IAM
```
