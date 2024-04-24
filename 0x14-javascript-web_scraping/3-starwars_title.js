#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const path = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(path, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  } else {
    console.error('Error:', error);
  }
});
