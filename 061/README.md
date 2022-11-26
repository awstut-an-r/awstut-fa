# AppSync – Data Source: RDS(Aurora Serverless)

https://awstut.com/en/2022/07/15/appsync-data-source-aurora-serverless-en/

# Architecture

![fa-061-diagram](https://user-images.githubusercontent.com/84276199/204085237-398536e4-2f1c-4baf-b30b-d2f0d10c9fdc.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-061.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare Lambda Layer Package

```bash
mkdir python

sudo pip3 install --pre gql[all] -t python

zip -r layer.zip python

aws s3 cp layer.zip s3://my-bucket/fa-061/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-061/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-061 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-061/fa-061.yaml \
--capabilities CAPABILITY_IAM
```
