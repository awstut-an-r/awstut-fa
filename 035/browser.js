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
const USER_POOL_ID = "ap-northeast-1_27X20ZW00";
const IDENTITY_POOL_ID = "ap-northeast-1:628252c8-3ed3-473d-9141-79bdf1cbd7ee";
const PARAMETER_NAME = "fa-035-authenticated";

const DOMAIN = "fa-035";
const CLIENT_ID = "2c45u7pnk8ubba6vf4otnubncv";
const REDIRECT_URI = "https://s3-ap-northeast-1.amazonaws.com/fa-035/signin.html";

const params = new URLSearchParams(window.location.search);
const code = params.get("code");

const tokenEndpoint = `https://${DOMAIN}.auth.${REGION}.amazoncognito.com/oauth2/token?grant_type=authorization_code&client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&code=${code}`;


const main = async () => {
  await fetch(tokenEndpoint, {
    method: "post",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    }})
    .then(response => {
      return response.json();
    })
    .then(data => {
      const idToken = data.id_token;
      
      const ssmClient = new SSMClient({
        region: REGION,
        credentials: fromCognitoIdentityPool({
          client: new CognitoIdentityClient({ region: REGION }),
          identityPoolId: IDENTITY_POOL_ID,
          logins: {
            [`cognito-idp.${REGION}.amazonaws.com/${USER_POOL_ID}`]: idToken
          }
        })
      });
      
      getParameter(ssmClient);
      getName(idToken);
    })
};

const getParameter = async (client) => {
  try {
    const response = await client.send(
      new GetParameterCommand({ Name: PARAMETER_NAME })
    );
    document.getElementById('parameter').innerText = `SSM Parameter Store: ${response.Parameter.Value}`;
  } catch (err) {
    console.log(err);
    document.getElementById('parameter').innerText = 'Deny access to SSM Parameter Store.';
  }
};

const getName = (idToken) => {
  try {
    const tokens = idToken.split('.');
    const tokenDecoded = JSON.parse(atob(tokens[1]));
    document.getElementById('name').innerText = `Name: ${tokenDecoded.name}`;
  } catch (err) {
    console.log(err);
    document.getElementById('name').innerText = 'Name: Guest';
  }
};

window.main = main;
