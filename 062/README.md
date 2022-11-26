# Initialize RDS DB with CFN Custom Resource

https://awstut.com/en/2022/07/16/initialize-rds-db-with-cfn-custom-resource-en/

# Architecture

![fa-062-diagram](https://user-images.githubusercontent.com/84276199/204086379-b2f2004a-6a16-4681-b0f7-ada59cdb0396.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-062.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Prepare Lambda Layer Package

```bash
mkdir python

pip3 install mysql-connector-python -t ./python

zip -r layer.zip python

aws s3 cp layer.zip s3://my-bucket/fa-062/
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-062/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-062 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-062/fa-062.yaml \
--capabilities CAPABILITY_IAM
```
