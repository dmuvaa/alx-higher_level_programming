#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);

  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
    process.exit(1);
  }

  return num1 + num2;
}

console.log(add(args[0], args[1]));
