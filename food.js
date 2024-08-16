const {google} = require('googleapis');;
const fs = require('fs').promises;
const path = require('path');
const process = require('process');
const CREDENTIALS_PATH = path.join(process.cwd(), 'credentials.json');

async function fetchCredentials(){
    const content = await fs.readFile(CREDENTIALS_PATH);
    const keys = JSON.parse(content);
    const key = keys.installed || keys.web;
    const auth = JSON.stringify({
        type: 'authorized_user',
        client_id: key.client_id,
        client_secret: key.client_secret,
        refresh_token: client.credentials.refresh_token,
    });
    return auth
}
const gmail = google.gmail({version: 'v1', fetchCredentials})
async function test(){
    console.log(await gmail.users.labels.get({
        "maxResults": 10,

        'userId': 'nyx2753@gmail.com',
        "id": "Expenses" 
    }))
}
test()