#!/usr/bin/node

const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Not a Number');
} else {
  console.log(`My number: ${Math.floor(num)}`);
}
