# Deliver S3 content via CloudFront using OAC

https://awstut.com/en/2022/11/27/deliver-s3-content-via-cloudfront-using-oac-en/

# Architecture

![fa-096-diagram](https://user-images.githubusercontent.com/84276199/204127626-8c48c3c0-279e-478b-820b-c87e4ad79d3f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-096.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-096/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-096 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-096/fa-096.yaml \
--capabilities CAPABILITY_IAM
```
