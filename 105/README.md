# Initial setup of DynamoDB with CFN custom resources

https://awstut.com/en/2022/12/28/initial-setup-of-dynamodb-with-cfn-custom-resources-en/

# Architecture

![fa-105-diagram](https://user-images.githubusercontent.com/84276199/209725697-ec39d2aa-efa7-48f1-8e05-0869e0dbee0d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-105.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-105/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-105 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-105/fa-105.yaml \
--capabilities CAPABILITY_IAM
```
