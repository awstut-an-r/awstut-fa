# Fargate Spot in CloudFormation

https://awstut.com/en/2022/10/16/fargate-spot-in-cloudformation-en/

# Architecture

![fa-090-diagram](https://user-images.githubusercontent.com/84276199/204132094-5a61b15e-aeec-49a1-b957-4a82b99a54ec.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-089.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-090/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-090 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-090/fa-090.yaml \
--capabilities CAPABILITY_IAM
```
