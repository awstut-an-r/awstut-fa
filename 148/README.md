# Automate OpenSearch Serverless indexing using CFN custom resources

https://awstut.com/en/2024/04/06/automate-opensearch-serverless-indexing-using-cfn-custom-resources-en/

# Architecture

![fa-148-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/ff69cd1f-ed7c-4293-82aa-2af06608da8a)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-148.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-148/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-148 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-148/fa-148.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
