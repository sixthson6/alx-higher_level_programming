#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (erro, response, body) => {
  console.log('code:', response && response.statusCode);
});
