# Use AWS Config to detect outdated access keys

https://awstut.com/en/2023/05/13/use-aws-config-to-detect-outdated-access-keys-en/

# Architecture

![fa-131-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/49a55f7f-9f82-484b-9943-9db684444d9d)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-131.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-131/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-131 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-131/fa-131.yaml \
--capabilities CAPABILITY_IAM
```
