# Use Secrets Manager to generate random password

https://awstut.com/en/2023/04/15/use-secrets-manager-to-generate-random-password-en/

# Architecture

![fa-126-diagram](https://user-images.githubusercontent.com/84276199/232220410-df194fce-21f4-49b5-b460-d138a6d6caf2.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-126.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-126/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-126 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-126/fa-126.yaml \
--capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```
