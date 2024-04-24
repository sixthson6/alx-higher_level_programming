#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const completed = {};
    const challenges = JSON.parse(body);
    challenges.forEach((challenge) => {
      if (challenge.completed && completed[challenge.userId] === undefined) {
        completed[challenge.userId] = 1;
      } else if (challenge.completed) {
        completed[challenge.userId] += 1;
      }
    });
    console.log(completed);
  } else {
    console.error('Error:', error);
  }
});
