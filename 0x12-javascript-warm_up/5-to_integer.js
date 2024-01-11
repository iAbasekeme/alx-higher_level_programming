#!/usr/bin/node

const process = require('process');
const arg = process.argv;
if (isNaN(parseInt(arg[2]))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg[2]));
}
