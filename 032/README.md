# Create apt Repository in S3 and access from private subnet

https://awstut.com/en/2022/06/19/create-apt-repository-in-s3-and-access-from-private-subnet-en/

# Architecture

![fa-032-diagram](https://user-images.githubusercontent.com/84276199/200165902-976351a8-27b3-46e2-bf5f-fda5e963fb09.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-032.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-032/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-032 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-031/fa-032.yaml \
--capabilities CAPABILITY_IAM
```
