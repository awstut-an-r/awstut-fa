# Create REST API type API Gateway using CFN

https://awstut.com/en/2022/05/22/create-rest-api-type-api-gateway-using-cloudformation-en/

# Architecture

![fa-052-diagram](https://user-images.githubusercontent.com/84276199/202889218-d2bfa713-fec2-4873-8910-03a24cb4f6d2.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-052.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-052/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-051 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-052/fa-052.yaml \
--capabilities CAPABILITY_IAM
```
