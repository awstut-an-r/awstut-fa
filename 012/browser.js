import {
  CognitoIdentityClient
} from "@aws-sdk/client-cognito-identity";

import {
  fromCognitoIdentityPool
} from "@aws-sdk/credential-provider-cognito-identity";

import {
  SSMClient,
  GetParameterCommand
} from "@aws-sdk/client-ssm";


// Set the parameter
const REGION = "ap-northeast-1";
const USER_POOL_ID = "ap-northeast-1_lFJAaM3qB";
const IDENTITY_POOL_ID = "ap-northeast-1:fce198d4-3cfd-4c03-9a74-c8c1fb2ea464";
const PARAMETER_NAME = "fa-012-authenticated";

const params = new URLSearchParams(location.hash.slice(1));
const idToken = params.get("id_token");

const ssmClient = new SSMClient({
  region: REGION,
  credentials: fromCognitoIdentityPool({
    client: new CognitoIdentityClient({ region: REGION }),
    identityPoolId: IDENTITY_POOL_ID,
    logins: {
      [`cognito-idp.${REGION}.amazonaws.com/${USER_POOL_ID}`]: idToken
    }
  }),
});

const getParameter = async () => {
  try {
    const response = await ssmClient.send(
      new GetParameterCommand({ Name: PARAMETER_NAME })
    );
    //console.log(response);
    document.getElementById('parameter').innerText = `SSM Parameter Store: ${response.Parameter.Value}`;
  } catch (err) {
    console.log(err);
    document.getElementById('parameter').innerText = 'Deny access to SSM Parameter Store.';
  }
};

const getName = async () => {
  try {
    const tokens = idToken.split('.');
    const tokenDecoded = JSON.parse(atob(tokens[1]));
    document.getElementById('name').innerText = `Name: ${tokenDecoded.name}`;
  } catch (err) {
    console.log(err);
    document.getElementById('name').innerText = 'Name: Guest';
  }
};

window.getParameter = getParameter;
window.getName = getName;