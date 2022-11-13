# AppSync – Data Source: Lambda

https://awstut.com/en/2022/05/05/appsync-data-source-lambda-en/

# Architecture

![fa-044-diagram](https://user-images.githubusercontent.com/84276199/201519506-ca525ac9-39fe-4e3e-86ac-a8d98dc7fe9f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-044.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare Lambda Functions Packages

```bash
zip deploy1.zip index.py
aws s3 cp deploy1.zip s3://my-bucket/fa-044/

zip deploy2.zip index.py
aws s3 cp deploy2.zip s3://my-bucket/fa-044/
```

## Prepare Lambda Layer Package

```bash
mkdir python
sudo pip3 install --pre gql[all] -t python
zip -r layer.zip python
aws s3 cp layer.zip s3://my-bucket/fa-044/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-044/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-044 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-044/fa-044.yaml \
--capabilities CAPABILITY_IAM
```
