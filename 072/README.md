# Enable Container Insights in Fargate and set alarms with traffic

https://awstut.com/en/2022/08/12/enable-container-insights-in-fargate-and-set-alarms-with-traffic-en/

# Architecture

![fa-072-diagram](https://user-images.githubusercontent.com/84276199/204113901-a0f267c6-b437-46e4-a84a-4d75e8003dca.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-072.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-072/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-072 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-072/fa-072.yaml \
--capabilities CAPABILITY_IAM
```
