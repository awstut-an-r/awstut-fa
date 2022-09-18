# Join Windows instance to AWS Managed Microsoft AD domain with SSM documentation

https://awstut.com/en/2022/01/16/join-windows-instance-to-aws-managed-microsoft-ad-domain-with-ssm-documentation/

# Architecture

![fa-017-diagram](https://user-images.githubusercontent.com/84276199/190901972-f2b012bc-4144-4f68-b231-dedc7b89c77b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-017.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-017/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-017 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-017/fa-017.yaml \
--capabilities CAPABILITY_IAM
```
