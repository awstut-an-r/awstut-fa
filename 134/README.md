# Register CloudFront + S3 configuration with Route53 and access with your own domain

https://awstut.com/en/2023/07/01/register-cloudfront-s3-configuration-with-route53-and-access-with-your-own-domain-en/

# Architecture

![fa-134-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/7191d3e2-e3d2-4e98-934e-032af62449bc)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-134.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-134/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-134 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-134/fa-134.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
