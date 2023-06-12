#!/usr/bin/node

const ArgNo = process.argv.length - 2;

if (ArgNo === 0) {
  console.log('No argument');
} else if (ArgNo === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
