# Setting up Test Units in CodePipeline

https://awstut.com/en/2022/09/18/setting-up-test-units-in-codepipeline-en/

# Architecture

![fa-081-diagram](https://user-images.githubusercontent.com/84276199/204130068-d43c5947-e511-4766-83b9-4abdb37d9103.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-081.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-081/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-081 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-081/fa-081.yaml \
--capabilities CAPABILITY_IAM
```
