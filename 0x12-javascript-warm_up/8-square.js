#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (isNaN(size)) {
  console.log('Missing size');
  process.exit(1);
}
