# Demonstrate remote actions (jobs) using Raspberry Pi and AWS IoT Device Client

https://awstut.com/en/2024/07/13/demonstrate-remote-actions-jobs-using-raspberry-pi-and-aws-iot-device-client-en/

# Architecture

![fa-156-diagram](https://github.com/user-attachments/assets/d1db10d1-f4b6-4a1d-908e-900a10993355)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in fa-156.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-156/ --recursive
```

## CloudFormation Stack Creation 1

```bash
aws cloudformation create-stack \
--stack-name fa-156-01 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-156/fa-156-01.yaml \
--capabilities CAPABILITY_IAM
```

 ## Raspberry Pi Setting up

```bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install libc6:armhf
mkdir /tmp/ssm
curl https://amazon-ssm-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/debian_arm/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
sudo chmod +x /tmp/ssm/ssm-setup-cli
sudo /tmp/ssm/ssm-setup-cli -register -activation-code "[activation-code]" -activation-id "[activation-id]" -region "ap-northeast-1"
```

## CloudFormation Stack Creation 2

```bash
aws cloudformation create-stack \
--stack-name fa-156-02 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-156/fa-156-02.yaml \
--capabilities CAPABILITY_IAM
```
