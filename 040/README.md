# Create Lambda layer using CFN

https://awstut.com/en/2022/04/29/create-lambda-layers-using-cloudformation-en/

# Architecture

![fa-040-diagram](https://user-images.githubusercontent.com/84276199/200169964-d70e553b-da05-413a-afe0-bbc1218e5901.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-040.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Create Lambda Layer Package

```bash
zip -r layer.zip python

aws s3 cp layer.zip s3://fa-040/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-040/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-040 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-040/fa-040.yaml \
--capabilities CAPABILITY_IAM
```
