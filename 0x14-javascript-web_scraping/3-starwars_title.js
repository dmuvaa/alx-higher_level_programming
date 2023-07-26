#!/usr/bin/node

// Import node libraries

const request = require('request');
const process = require('process');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
