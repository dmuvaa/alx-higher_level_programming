#!/usr/bin/node

const Arg1 = process.argv[2];

if (Arg1 === undefined) {
  console.log('No argument');
} else {
  console.log(Arg1);
}
