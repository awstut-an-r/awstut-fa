# Upload/download files to/from S3 with Presigned URL

https://awstut.com/en/2022/12/30/upload-download-files-to-from-s3-with-presigned-url-en/

# Architecture

![fa-106-diagram](https://user-images.githubusercontent.com/84276199/210019846-72649315-53fd-4e8d-bd0c-5bd916291359.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-106.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-106/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-106 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-106/fa-106.yaml \
--capabilities CAPABILITY_IAM
```
