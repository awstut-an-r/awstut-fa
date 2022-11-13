# Geographic Restrictions using WAF Web ACL

https://awstut.com/en/2022/05/07/geographic-restrictions-using-waf-web-acl-en/

# Architecture

![fa-046-diagram](https://user-images.githubusercontent.com/84276199/201520878-172f850e-b082-4235-a7c7-064be9556301.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-046.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-046/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-046 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-046/fa-046.yaml \
--capabilities CAPABILITY_IAM
```
