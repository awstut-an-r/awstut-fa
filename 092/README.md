# Separate Web and App Servers Using Internal NLB – Apache Ver.

https://awstut.com/en/2022/11/03/separate-web-and-app-servers-using-internal-nlb-apache-en/

# Architecture

![fa-092-diagram](https://user-images.githubusercontent.com/84276199/204132324-bb3bd438-8318-453b-8f17-4560ab2e8830.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-092.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-092/ --recursive
```

## Upload Playbook Files

```bash
zip -r playbook.zip ./playbook/*

aws s3 cp playbook.zip s3://my-bucket/
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-092 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-092/fa-092.yaml \
--capabilities CAPABILITY_IAM
```
