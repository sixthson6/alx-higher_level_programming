#!/usr/bin/node

const request = require('request');
const path = process.argv[2];

request(path, (error, response, body) => {
  console.log('code:', response && response.statusCode);
});
