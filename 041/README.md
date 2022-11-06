# Introduction to AppSync with CFN – Data Source: DynamoDB

https://awstut.com/en/2022/05/02/introduction-to-appsync-with-cloudformation-en/

# Architecture

![fa-041-diagram](https://user-images.githubusercontent.com/84276199/200170475-17187aef-72bb-42da-9041-6561bb3e7636.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-041.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Create Lambda Layer Package

```bash
pip3 install --pre gql[all] -t python

zip -r layer.zip python

aws s3 cp layer.zip s3://my-bucket/fa-041/
```

## Create Lambda Function Packages

```bash
zip -r deploy1.zip index.py
zip -r deploy2.zip index.py
zip -r deploy3.zip index.py

aws s3 cp deploy1.zip s3://my-bucket/fa-041/
aws s3 cp deploy2.zip s3://my-bucket/fa-041/
aws s3 cp deploy3.zip s3://my-bucket/fa-041/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-041/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-041 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-041/fa-041.yaml \
--capabilities CAPABILITY_IAM
```
