#!/usr/bin/node
const request = require('request')
const arg = process.argv[2]

request(arg, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: '+ response.statusCode);
  }
});
