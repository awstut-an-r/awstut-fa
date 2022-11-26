# AppSync – Data Source: None

https://awstut.com/en/2022/05/28/appsync-datasource-none-en/

# Architecture

![fa-054-diagram](https://user-images.githubusercontent.com/84276199/202889537-77aac6e0-5c9c-470f-ab20-181945217503.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-054.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare Lambda Function Package

```bash
zip deploy.zip index.py

aws s3 cp deploy.zip s3://my-bucket/fa-054/
```

## Prepare Lambda Layer Package

```bash
mkdir python

sudo pip3 install --pre gql[all] -t python

zip -r layer.zip python

aws s3 cp layer.zip s3://my-bucket/fa-054/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-054/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-054 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-054/fa-054.yaml \
--capabilities CAPABILITY_IAM
```
