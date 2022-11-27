# Deleting NAT Gateway used only during initial build with CFN custom resource

https://awstut.com/en/2022/08/06/deleting-nat-gateway-used-only-during-initial-build-with-cfn-custom-resource-en/

# Architecture

![fa-071-diagram](https://user-images.githubusercontent.com/84276199/204113797-e6c326ed-079d-4059-91a7-8f767d2ffeb3.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-071.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-071/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-071 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-071/fa-071.yaml \
--capabilities CAPABILITY_IAM
```
