# Apply WAF Web ACL to AppSync

https://awstut.com/en/2022/05/29/apply-waf-web-acl-to-appsync-en/

# Architecture

![fa-055-diagram](https://user-images.githubusercontent.com/84276199/202889964-56df4440-2bb5-40de-8302-0eec613c7f2e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-055.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare Lambda Function Package

```bash
zip deploy.zip index.py

aws s3 cp deploy.zip s3://my-bucket/fa-055/
```

## Prepare Lambda Layer Package

```bash
mkdir python

sudo pip3 install --pre gql[all] -t python

zip -r layer.zip python

aws s3 cp layer.zip s3://my-bucket/fa-055/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-055/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-055 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-055/fa-055.yaml \
--capabilities CAPABILITY_IAM
```
