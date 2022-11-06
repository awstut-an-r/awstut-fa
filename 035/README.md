# Authorization by Cognito ID Pool after Authentication by User Pool – Authorization grant code ver

https://awstut.com/en/2022/04/02/authorization-by-cognito-id-pool-after-authentication-by-user-pool-authorization-grant-code/

# Architecture

![fa-035-diagram](https://user-images.githubusercontent.com/84276199/200167361-26bb20af-56b9-41b9-ae37-1a46b3715e7f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-035.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-035/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-035 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-035/fa-035.yaml \
--capabilities CAPABILITY_IAM
```

## Build main.js

https://awstut.com/en/2022/04/02/authorization-by-cognito-id-pool-after-authentication-by-user-pool-authorization-grant-code/

## Upload index.html and main.js

```bash
aws s3 cp ./html s3://fa-035/

aws s3 cp main.js s3://fa-035/
```
