# Serverless apps using SAM

https://awstut.com/en/2021/12/12/serverless-apps-using-sam/

# Architecture

![fa-006-diagram](https://user-images.githubusercontent.com/84276199/188433568-a87a9dd5-91f7-4be2-bc71-bfab6bc49f8e.png)

# Requirements

* AWS SAM CLI

# Usage

## SAM App Creation

```bash
$ sam init
Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1
What package type would you like to use?
        1 - Zip (artifact is a zip uploaded to S3)
        2 - Image (artifact is an image uploaded to an ECR image repository)
Package type: 1

Which runtime would you like to use?
        1 - nodejs12.x
        2 - python3.8
        3 - ruby2.7
        4 - go1.x
        5 - java11
        6 - dotnetcore3.1
        7 - nodejs10.x
        8 - python3.7
        9 - python3.6
        10 - python2.7
        11 - ruby2.5
        12 - java8.al2
        13 - java8
        14 - dotnetcore2.1
Runtime: 2

Project name [sam-app]: fa-006

Cloning app templates from https://github.com/aws/aws-sam-cli-app-templates

AWS quick start application templates:
        1 - Hello World Example
        2 - EventBridge Hello World
        3 - EventBridge App from scratch (100+ Event Schemas)
        4 - Step Functions Sample App (Stock Trader)
        5 - Elastic File System Sample App
Template selection: 1

    -----------------------
    Generating application:
    -----------------------
    Name: fa-006
    Runtime: python3.8
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .
```

## Replace SAM Template

```bash
mv template.yaml fa-006
```

## Build SAM App

```bash
sam build --use-container
```

## Deploy SAM App

```bash
sam deploy --guided
```
