#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});

