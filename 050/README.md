# S3 content delivery via CloudFront – OAI ver

https://awstut.com/en/2022/05/16/s3-content-delivery-via-cloudfront-oai-en/

# Architecture

![fa-050-diagram-01](https://user-images.githubusercontent.com/84276199/202888808-b0ea7d1f-d48d-415b-a1fb-3e5a722cebd6.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-050.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-050/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-050 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-050/fa-050.yaml \
--capabilities CAPABILITY_IAM
```
