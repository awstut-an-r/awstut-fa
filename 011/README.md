# Publish your site with S3 static website hosting

https://awstut.com/en/2021/12/12/publish-your-site-with-s3-static-website-hosting/

# Architecture

![fa-011-diagram](https://user-images.githubusercontent.com/84276199/189878618-3ed882c9-e9b7-4897-86de-9c7decbcde86.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-011.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-011/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-011 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-011/fa-011.yaml \
--capabilities CAPABILITY_IAM
```

## Upload HTML files

```bash
aws s3 cp ./html s3://fa-011-bucket/ --recursive
```
