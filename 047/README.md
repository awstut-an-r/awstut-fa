# Create and Delete S3 Object by CloudFormation Custom Resource

https://awstut.com/en/2022/05/08/create-and-delete-s3-object-by-cfn-custom-resource-en/

# Architecture

![fa-047-diagram](https://user-images.githubusercontent.com/84276199/201790250-89cfa88d-2cee-4302-a271-e287469b9f09.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-047.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-047/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-047 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-047/fa-047.yaml \
--capabilities CAPABILITY_IAM
```
