#!/usr/bin/node

// Import key node libraries

const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;

    results.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes('18')) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
