# Use CodePipeline to build and deploy images to Fargate

https://awstut.com/en/2022/08/20/use-codepipeline-to-build-and-deploy-images-to-fargate-en/

# Architecture

![fa-076-diagram](https://user-images.githubusercontent.com/84276199/204114993-4e655ea9-d3e6-4b2f-976a-04f6a11e972d.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-076.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp ./templates s3://my-bucket/fa-076/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-076 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-076/fa-076.yaml \
--capabilities CAPABILITY_IAM
```
