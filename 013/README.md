# CloudFormation’s nested stack

https://awstut.com/en/2021/12/11/cloudformations-nested-stack/

# Architecture

![fa-013-diagram](https://user-images.githubusercontent.com/84276199/189880066-1cc9b7de-3155-454e-958b-055a16e4b053.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-013.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-013/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-013 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-013/fa-013.yaml \
--capabilities CAPABILITY_IAM
```
