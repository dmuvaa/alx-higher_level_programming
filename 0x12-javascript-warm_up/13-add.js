#!/usr/bin/node

fuction add(a, b) {
  let num1 = parseInt(a);
  let num2 = parseInt(b);

  if (isNaN(num1) || isNaN(num2)) {
    return "isNaN";
  }

  return num1 + num2;
}
