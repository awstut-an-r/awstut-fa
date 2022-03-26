//const {
//  CognitoIdentityClient
//} = require("@aws-sdk/client-cognito-identity");
//
//const {
//  fromCognitoIdentityPool
//} = require("@aws-sdk/credential-provider-cognito-identity");
//
//const {
//  LambdaClient,
//  InvokeCommand,
//} = require("@aws-sdk/client-lambda");
//
//const {
//  toUtf8
//} = require("@aws-sdk/util-utf8-browser");

import {
  CognitoIdentityClient
} from "@aws-sdk/client-cognito-identity";

import {
  fromCognitoIdentityPool
} from "@aws-sdk/credential-provider-cognito-identity";

import {
  LambdaClient,
  InvokeCommand
} from "@aws-sdk/client-lambda";

import {
  toUtf8
} from "@aws-sdk/util-utf8-browser";


// Set the parameter
const REGION = "ap-northeast-1";
const IDENTITY_POOL_ID = "ap-northeast-1:f78ed244-a960-481d-b20d-54649660f668";
const FUNCTION_NAME = "fa-034-function";
//const ACCOUNT_ID = "ACCOUNT_ID";

const lambdaClient = new LambdaClient({
  region: REGION,
  credentials: fromCognitoIdentityPool({
    client: new CognitoIdentityClient({ region: REGION }),
    identityPoolId: IDENTITY_POOL_ID
  }),
});

const showLambdaResult = async () => {
  try {
    const response = await lambdaClient.send(
      new InvokeCommand({ FunctionName: FUNCTION_NAME })
    );
    //console.log(response.Payload);
    //console.log(toUtf8(response.Payload));
    document.getElementById("viewer").innerHTML = `<p>${toUtf8(response.Payload)}</p>`
  } catch (err) {
    console.log(err);
  }
};

window.showLambdaResult = showLambdaResult;