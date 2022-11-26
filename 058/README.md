# Aurora Serverless with CFN

https://awstut.com/en/2022/06/04/apply-waf-web-acl-to-api-gateway-en/

# Architecture

![fa-058-diagram](https://user-images.githubusercontent.com/84276199/204084530-3c6ff723-0618-4ab7-b102-1e8119da44da.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-058.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-058/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-058 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-058/fa-058.yaml \
--capabilities CAPABILITY_IAM
```
