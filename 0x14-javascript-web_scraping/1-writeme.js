#!/usr/bin/node
const fs = require('fs')
const arg = process.argv[2]
const stringPath = process.argv[3]

fs.writeFile(arg, stringPath, 'utf-8', (err) => {
  if (err) {
    return console.error(err)
  }
})
