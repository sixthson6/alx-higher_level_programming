#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, 'utf8', (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    /* console.log(filmsData); */
    let count = 0;
    filmsData.results.forEach((film) => {
      film.characters.forEach((characterUrl) => {
        if (characterUrl === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count++;
        }
      });
    });
    console.log(count);
  } else {
    console.error('Error:', error);
  }
});
