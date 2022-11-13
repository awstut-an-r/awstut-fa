# Introduction to WAF Web ACL with CNF – ALB Ver.

https://awstut.com/en/2022/05/06/introduction-to-waf-web-acl-with-cloudformation-en/

# Architecture

![fa-045-diagram](https://user-images.githubusercontent.com/84276199/201519835-ec643df4-3680-4f1e-9816-2f4450eb1f2d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-045.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-045/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-045 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-045/fa-045.yaml \
--capabilities CAPABILITY_IAM
```
