# Lambda Function URL by CFN – Auth Type: NONE

https://awstut.com/en/2022/04/24/lambda-function-url-by-cloudformation-auth-type-none-en/

# Architecture

![fa-038-diagram](https://user-images.githubusercontent.com/84276199/200168574-5be7b034-8d6b-41bb-9bdf-57e294f82607.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-038.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-038/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-038 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-038/fa-038.yaml \
--capabilities CAPABILITY_IAM
```
