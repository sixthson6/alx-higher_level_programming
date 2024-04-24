#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    /* const siteData = JSON.parse(body); */
    fs.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.error('Error:', error);
      }
    });
  }
});
