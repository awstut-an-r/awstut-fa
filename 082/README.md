# Enable image scanning at ECR repository level

https://awstut.com/en/2022/09/19/enable-image-scanning-at-ecr-repository-level-en/

# Architecture

![fa-082-diagram](https://user-images.githubusercontent.com/84276199/204130175-d091f85c-8575-4c4c-aa2c-196230c46f60.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-082.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-082/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-082 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-082/fa-082.yaml \
--capabilities CAPABILITY_IAM
```
