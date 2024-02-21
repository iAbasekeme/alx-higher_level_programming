#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
const fs = require('fs');
const file = process.argv[3]
const page = process.argv[2]

request(page, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.body);
  }
})