#!/usr/bin/node
const request = require('require');
const arg = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/'
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body));
  }
});