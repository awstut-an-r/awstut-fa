# Use TaskCat to automate testing of CloudFormation templates

https://awstut.com/en/2023/07/22/use-taskcat-to-automate-testing-of-cloudformation-templates-en/

# Architecture

![fa-137-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/e4904ff5-651b-4671-aa58-dcd65f579f1f)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-137.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]

  MailAddress:
    Type: String
    Default: [mail-address]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-137/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-137 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-137/fa-137.yaml \
--capabilities CAPABILITY_IAM
```
