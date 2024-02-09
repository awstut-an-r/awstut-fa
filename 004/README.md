# Four ways to initialize Linux instance

https://awstut.com/en/2021/12/11/four-ways-to-initialize-a-linux-instance/

# Architecture

![fa-004-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/0ba41ff6-8805-4e25-9d41-45e092e19a71)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-004.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload Playbook and Template Files to S3 Bucket

```bash
zip -r playbook.zip playbook.yml
aws s3 cp . s3://my-bucket/fa-004/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-004 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-004/fa-004.yaml \
--capabilities CAPABILITY_IAM
```
