# S3 content delivery via CloudFront – Referer hreader ver

https://awstut.com/en/2022/05/15/s3-content-delivery-via-cloudfront-referer-hreader-en/

# Architecture

![fa-049-diagram](https://user-images.githubusercontent.com/84276199/202888689-ce095ef0-3d5d-4982-9e20-6548753408d3.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-049.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-049/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-049 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-049/fa-049.yaml \
--capabilities CAPABILITY_IAM
```
