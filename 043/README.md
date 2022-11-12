# Introduction to CloudFormation Custom Resources

https://awstut.com/en/2022/05/04/introduction-to-cloudformation-custom-resources-en/

# Architecture

![fa-043-diagram](https://user-images.githubusercontent.com/84276199/201472125-ab67b6a6-7490-493d-aeb0-46493af28b95.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-043.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-043/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-043 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-043/fa-043.yaml \
--capabilities CAPABILITY_IAM
```
