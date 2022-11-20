# S3 content delivery via CloudFront – Static website hosting ver

https://awstut.com/en/2022/05/14/s3-content-delivery-via-cloudfront-static-website-hosting-ver-en/

# Architecture

![fa-048-diagram](https://user-images.githubusercontent.com/84276199/202888581-caea5303-b723-4d8c-b152-42073eec1282.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-048.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-048/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-048 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-048/fa-048.yaml \
--capabilities CAPABILITY_IAM
```
