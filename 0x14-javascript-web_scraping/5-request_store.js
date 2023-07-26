#!/usr/bin/node

// Import node libraries

const fs = require('fs');
const request = require('request');
const process = require('process');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    return console.error('Error:', error);
  }

  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      return console.error('Error:', err);
    }
  });
});
