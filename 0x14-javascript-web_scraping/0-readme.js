#!/usr/bin/node
const fs = require('fs')
const arg = process.argv[2]

// Synchronously read the file
fs.readFile(arg, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
