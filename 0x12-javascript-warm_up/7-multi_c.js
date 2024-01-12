#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (parseInt(args[2])) {
  let i = 0;
  for (; i < args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
