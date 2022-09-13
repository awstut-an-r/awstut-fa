# Authorization by Cognito ID Pool after Authentication by User Pool – Implicit Grant Ver

https://awstut.com/en/2021/12/12/granting-credentials-to-authenticated-users-in-cognito-id-pool/

# Architecture

![fa-012-diagram](https://user-images.githubusercontent.com/84276199/189879155-74dce68f-8864-4ca5-b806-56c94840fb9f.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)
* npm

# Usage

## Tempalte File Modification

Modify the following locations in fa-010.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: my-bucket
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/fa-012/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name fa-012 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/fa-012/fa-012.yaml \
--capabilities CAPABILITY_IAM
```

## JavaScript Browser Script Creation

https://awstut.com/en/2022/03/27/using-aws-sdk-for-javascript-v3-in-browser/

### npm Initialization

```bash
npm init
npm install --save-dev webpac
npm install --save-dev path-browserify
```

### Modify webpack.config.js

Correct the values of "entry" and "filename".

```js
var path = require("path");
module.exports = {
  entry: [path.join(__dirname, "browser.js")],
  output: {
    path: __dirname,
    filename: 'main.js'
  },
   resolve:{
  fallback: { path: require.resolve("path-browserify")}
  }
};
```

### Modify package.json

Correct the values of "build".

```json
{
  "name": "034",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "path-browserify": "^1.0.1",
    "webpack": "^5.70.0"
  }
}
```

## Install SDK for JavaScript

```bash
npm install @aws-sdk/client-cognito-identity

npm install @aws-sdk/credential-provider-cognito-identity

npm install @aws-sdk/client-ssm
```

## Build Browser Script

Build main.js from SDK and browser.js.

```bash
npm run build
```

## Upload HTML and JavaScript files

```bash
aws s3 cp ./html s3://fa-012/ --recursive

aws s3 cp main.js s3://fa-012/
```
