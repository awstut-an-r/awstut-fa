# 5 patterns of OAuth scopes for Cognito User Pool

https://awstut.com/en/2022/04/03/oauth-scopes-for-cognito-user-pool/

# Architecture

![fa-036-diagram](https://user-images.githubusercontent.com/84276199/200167586-bd3e5b0f-b06c-43fa-b5e1-f9d26fbfd2ca.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-036.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-036/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-036 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-036/fa-036.yaml \
--capabilities CAPABILITY_IAM
```

## Build main.js

https://awstut.com/en/2022/04/03/oauth-scopes-for-cognito-user-pool/

## Upload index.html and main.js

```bash
aws s3 cp index.html s3://fa-036/

aws s3 cp main.js s3://fa-036/
```
