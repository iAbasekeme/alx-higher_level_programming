#!/usr/bin/node
const request = require('request')
const arg = process.argv[2]

request(arg, (response) => {
  console.log(response.statusCode);
})