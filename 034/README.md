# Using AWS SDK for JavaScript v3 in Browser

https://awstut.com/en/2022/03/27/using-aws-sdk-for-javascript-v3-in-browser/

# Architecture

![fa-034-diagram](https://user-images.githubusercontent.com/84276199/200166684-a6bd523d-16c5-4904-8c4a-4461a5dd20c0.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-034.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-034/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-034 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-034/fa-034.yaml \
--capabilities CAPABILITY_IAM
```

## Build main.js

https://awstut.com/en/2022/03/27/using-aws-sdk-for-javascript-v3-in-browser/

## Upload index.html and main.js

```bash
aws s3 cp index.html s3://fa-034/

aws s3 cp main.js s3://fa-034/
```
