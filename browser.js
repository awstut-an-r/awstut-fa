/*
import {
  CognitoIdentityClient
} from "@aws-sdk/client-cognito-identity";

import {
  fromCognitoIdentity
} from "@aws-sdk/credential-provider-cognito-identity";
*/

import {
  CognitoIdentityProviderClient,
  GetUserCommand
} from "@aws-sdk/client-cognito-identity-provider";


const getPayloadFromJWT = (token) => {
  return token.split(".")[1]
};


const REGION = "ap-northeast-1";
const USER_POOL_ID = "ap-northeast-1_nd984pe0j";
//const USER_NAME = "awstut";

const params = new URLSearchParams(location.hash.slice(1));
const accessToken = params.get("access_token");
const idToken = params.get("id_token");

const showAccessToken = () => {
  //console.log(accessToken);
  document.getElementById("access-token").innerText = JSON.stringify(
    JSON.parse(atob(getPayloadFromJWT(accessToken))), null , 2);
};

const showIdToken = () => {
  if (idToken !== null) {
    //console.log(idToken);
    document.getElementById("id-token").innerText = JSON.stringify(
      JSON.parse(atob(getPayloadFromJWT(idToken))), null , 2);
  } else {
    document.getElementById("id-token").innerText = "No ID Token.";
  }
};

const client = new CognitoIdentityProviderClient({
  region: REGION
});

const showUser = async () => {
  try {
    const response = await client.send(
      new GetUserCommand({
        AccessToken: accessToken
      })
    );
    //console.log(response);
    document.getElementById("get-user").innerText = JSON.stringify(response, null, 2);
  } catch (err) {
    //console.log(err);
    document.getElementById("get-user").innerText = JSON.stringify(err, null, 2);
  }
}

showAccessToken();
showIdToken();
showUser();