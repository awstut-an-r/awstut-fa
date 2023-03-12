# Iteration using Map in Step Functions

https://awstut.com/en/2023/03/12/iteration-using-map-in-step-functions-en/

# Architecture

![fa-121-diagram](https://user-images.githubusercontent.com/84276199/224534490-fd633977-56e3-488b-a52e-5fdade254d25.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-121.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-121/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-121 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-121/fa-121.yaml \
--capabilities CAPABILITY_IAM
```
