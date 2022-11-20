# Apply WAF Web ACL to API Gateway

https://awstut.com/en/2022/06/04/apply-waf-web-acl-to-api-gateway-en/

# Architecture

![fa-053-diagram](https://user-images.githubusercontent.com/84276199/202889403-08357f4b-dda7-494a-98e2-a5671826883d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-053.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-053/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-053 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-053/fa-053.yaml \
--capabilities CAPABILITY_IAM
```
