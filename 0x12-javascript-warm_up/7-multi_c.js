#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}

for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
