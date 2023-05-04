# Preparing Lambda Layer Package with CFN Custom Resources – General File Version

https://awstut.com/en/2023/05/05/preparing-lambda-layer-package-with-cfn-custom-resources-general-file-version-en/

# Architecture

![fa-130-diagram](https://user-images.githubusercontent.com/84276199/236341607-f1a1e6fe-f495-48fc-b439-722af84a3008.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-130.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-130/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-130 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-130/fa-130.yaml \
--capabilities CAPABILITY_IAM
```
