# 3-Tier Architecture with Apache/Python(uWSGI)/RDS(Aurora)

https://awstut.com/en/2022/11/20/3-tier-architecture-with-apache-python-uwsgi-rds-aurora-en/

# Architecture

![fa-094-diagram](https://user-images.githubusercontent.com/84276199/204133160-47e6f98d-cdda-4e03-bf00-e82597b864cb.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-094.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-094/ --recursive
```

## Upload Playbook Files

```bash
zip -r playbook.zip ./playbook/*

aws s3 cp playbook.zip s3://my-bucket/
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-094 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-094/fa-094.yaml \
--capabilities CAPABILITY_IAM
```
