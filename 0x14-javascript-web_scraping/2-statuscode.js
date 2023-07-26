#!/usr/bin/node

// import necessary libraries in Node

const request = require('request');
const process = require('process');

const url = process.argv[2];

request
  .get(url)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  })
  .on('error', function (err) {
    console.error(err);
  });
