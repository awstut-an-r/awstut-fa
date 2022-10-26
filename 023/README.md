# On SSL your own domain using ACM Certificate

https://awstut.com/en/2022/02/12/on-ssl-your-own-domain-using-acm-certificate-2/

# Architecture

![fa-023-diagram](https://user-images.githubusercontent.com/84276199/198046326-972a28b6-d4da-4bb8-8d8b-105c8bfee72c.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Register domain name

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html

## Tempalte File Modification

Modify the following locations in fa-023.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
    
  ALBHostedZoneId:
    Type: String
    Default: [alb-hosted-zone-id]
    
  DomainName:
    Type: String
    Default: [domain-name]
    
  HostedZoneId:
    Type: String
    Default: [hosted-zone-id]
```

Check the HostedZoneId of ALB at the following page.

https://docs.aws.amazon.com/general/latest/gr/elb.html

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-023/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-023 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-023/fa-023.yaml \
--capabilities CAPABILITY_IAM
```
