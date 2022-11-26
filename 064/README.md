# Preparing Lambda Layer Package with CFN Custom Resources – Python Version

https://awstut.com/en/2022/07/18/preparing-lambda-layer-package-with-cfn-custom-resources-python-version-en/

# Architecture

![fa-064-diagram](https://user-images.githubusercontent.com/84276199/204087626-d930be50-162e-423e-ab5d-6e5a4390f28b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-064.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-064/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-064 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-064/fa-064.yaml \
--capabilities CAPABILITY_IAM
```
