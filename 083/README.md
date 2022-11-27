# Enable image scanning at ECR registry level

https://awstut.com/en/2022/09/23/enable-image-scanning-at-ecr-registry-level-en/

# Architecture

![fa-083-diagram](https://user-images.githubusercontent.com/84276199/204130352-d0ec6e7c-d047-4e07-9733-2889a4193c3b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-083.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-083/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-083 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-083/fa-083.yaml \
--capabilities CAPABILITY_IAM
```
