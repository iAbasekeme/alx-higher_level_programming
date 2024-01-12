#!/usr/bin/node

const process = require('process');
const arg = process.argv;
const n = 5;
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial ( n - 1 );
  }
}
if (parseInt(arg[2])) {
  const num = arg[2];
  console.log(factorial(num));
} else {
  console.log('1');
}
