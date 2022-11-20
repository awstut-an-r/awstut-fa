# Apply WAF Web ACL to CloudFront

https://awstut.com/en/2022/05/22/apply-waf-web-acl-to-cloudfront-en/

# Architecture

![fa-051-diagram](https://user-images.githubusercontent.com/84276199/202888997-cce27a0f-fb8d-428c-a612-405291b43dd9.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *us-east-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-051.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-051/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-051 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-051/fa-051.yaml \
--capabilities CAPABILITY_IAM
```
