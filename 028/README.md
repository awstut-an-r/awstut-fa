# Three target types of ALB (Instance, IP, Lambda) and Auto Scaling

https://awstut.com/en/2022/02/26/three-target-types-of-alb-2/

# Architecture

![fa-028-diagram](https://user-images.githubusercontent.com/84276199/200163402-006daca3-0bf6-4de2-9af7-95bd936f7558.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-028.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-028/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-028 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-028/fa-028.yaml \
--capabilities CAPABILITY_IAM
```
