# Introduction to OpenSearch with CFN

https://awstut.com/en/2022/05/03/introduction-to-opensearch-with-cloudformation-en/

# Architecture

![fa-042-diagram](https://user-images.githubusercontent.com/84276199/201461521-ed067a1c-22e3-49eb-bbcf-6024c2f43ade.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-042.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-042/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-042 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-042/fa-042.yaml \
--capabilities CAPABILITY_IAM
```

## Upload data

```bash
curl -XPUT -u '[username]:[password]' 'https://[opensearch-domain]/fa-042/_doc/1' -d '{"director": "Burton, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}' -H 'Content-Type: application/json'
```

## Search OpenSearch

```bash
curl -XGET -u '[username]:[password]' 'https://[opensearch-domain]/fa-042/_search?q=mars&pretty=true'
```
