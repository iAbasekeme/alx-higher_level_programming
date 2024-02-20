#!/usr/bin/node
const fs = require('fs')
const arg = process.argv[2]

// Synchronously read the file
fs.readFile(arg, 'utf8', (err, data) => {
    if (err) {
        return console.error(err)
    }
    console.log(data)
})
