# Install CloudWatch Agent on Windows and collect data

https://awstut.com/en/2021/12/28/install-cloudwatch-agent-on-windows-and-collect-data/

# Architecture

![fa-016-diagram](https://user-images.githubusercontent.com/84276199/190859401-94d37df6-7b89-4c81-a8ca-fadf5eefa623.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-016.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-016/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-016 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-016/fa-016.yaml \
--capabilities CAPABILITY_IAM
```
