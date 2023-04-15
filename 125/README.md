# All patterns of server-side encryption of S3 buckets – SSE-S3/SSE-KMS/SSE-C

https://awstut.com/en/2023/04/16/all-patterns-of-server-side-encryption-of-s3-buckets-sse-s3-sse-kms-sse-c-en/

# Architecture

![fa-125-diagram](https://user-images.githubusercontent.com/84276199/232256053-758b52eb-934b-4d1e-add4-a24a709786b7.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-125.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-125/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-125 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-125/fa-125.yaml \
--capabilities CAPABILITY_IAM
```
