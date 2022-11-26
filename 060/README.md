# Initialize DB on Aurora Serverless with Data API enabled using CFN Custom Resource

https://awstut.com/en/2022/07/10/initialize-db-on-aurora-serverless-with-data-api-enabled-using-cfn-custom-resource-en/

# Architecture

![fa-060-diagram](https://user-images.githubusercontent.com/84276199/204084959-93ab6e3d-5aee-45a1-801f-50fd10d8c7ef.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-060.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-060/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-060 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-060/fa-060.yaml \
--capabilities CAPABILITY_IAM
```
