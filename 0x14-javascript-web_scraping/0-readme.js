#!/usr/bin/node
var fs = require('fs')
var arg = process.argv[2]

// Synchronously read the file
fs.readFile(arg, 'utf8', (err, data) => {
    if (err) {
        return console.error(err)
    }
    console.log(data)
})
