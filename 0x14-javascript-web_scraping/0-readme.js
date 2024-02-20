#!/usr/bin/node
var fs = require('fs')
var arg = process.argv[1]

try {
    // Synchronously read the file
    const data = fs.readFile(arg, 'utf8')
    console.log(data);
} catch (err) {
    // Handle the errors
    console.error(err)
}
