#!/usr/bin/node

// Import built in Node libraries

const fs = require('fs');
const process = require('process');

// Create filepath process
const filePath = process.argv[2];

try {
  const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
