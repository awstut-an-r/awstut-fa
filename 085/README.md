# Introduction to ECR Repository Policies Using CFN

https://awstut.com/en/2022/09/24/introduction-to-ecr-repository-policies-using-cfn-en/

# Architecture

![fa-084-diagram](https://user-images.githubusercontent.com/84276199/204130502-6b18bb61-86cf-444c-bff9-c020a9c56088.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-085.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-085/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-085 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-085/fa-085.yaml \
--capabilities CAPABILITY_IAM
```
