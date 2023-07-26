#!/usr/bin/node

// Import modules from Node Library
const fs = require('fs');
const process = require('process');

// First Argument
const filePath = process.argv[2];
const content = process.argv[3];

try {
  fs.writeFileSync(filePath, content, 'utf-8');
} catch (err) {
  console.log(err);
}
