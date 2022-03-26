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
const IDENTITY_POOL_ID = "[ID of Cognito ID Pool]";
const FUNCTION_NAME = "[Lambda Function Name]";

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
    document.getElementById("viewer").innerHTML = `<p>${toUtf8(response.Payload)}</p>`
  } catch (err) {
    console.log(err);
  }
};

window.showLambdaResult = showLambdaResult;
