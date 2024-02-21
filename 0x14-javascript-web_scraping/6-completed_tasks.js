#!/usr/bin/node
const { error } = require('console');
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(response.body);
})
