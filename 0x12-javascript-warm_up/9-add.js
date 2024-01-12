#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const process = require('process');
const args = process.argv;

if (parseInt(args[2]) && parseInt(args[3])) {
  const num1 = parseInt(args[2]);
  const num2 = parseInt(args[3]);

  if (!isNaN(num1) && !isNaN(num2)) {
    console.log(add(num1, num2));
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
