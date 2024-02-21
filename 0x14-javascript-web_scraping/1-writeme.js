#!/usr/bin/node
const { error } = require('console')
const fs = require('fs')
const arg = process.argv[2]
const string_path = process.argv[3]

fs.writeFile(arg, string_path, 'utf-8', (err) => {
  if(err) {
    return console.error(err)
  }
})