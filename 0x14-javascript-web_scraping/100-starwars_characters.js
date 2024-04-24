#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const names = JSON.parse(body);
    names.characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const chars = JSON.parse(body);
          console.log(chars.name);
        }
      });
    });
  } else {
    console.error(error);
  }
});
