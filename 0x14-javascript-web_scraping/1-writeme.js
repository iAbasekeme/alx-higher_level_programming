#!/usr/bin/node
const arg = process.argv[2]
const stringPath = process.argv[3]
const fs = require('fs')

fs.writeFile(arg, stringPath, 'utf-8', function (err) {
  if (err) {
    return console.error(err);
  }
});
