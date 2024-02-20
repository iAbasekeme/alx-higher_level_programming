#!/usr/bin/node
var fs = require('fs')
var arg = process.argv[1]

// Synchronously read the file
fs.readFile(arg, 'utf8', (err, data) => {
    if (err) {
    // Handle the errors
    	return console.error(err)
    }
     console.log(data)
})

