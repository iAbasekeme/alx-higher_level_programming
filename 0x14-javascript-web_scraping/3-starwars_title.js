#!/usr/bin/node
const { url } = require('inspector');
const request = require('request');
const arg = process.argv[2];

url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
request(url, (error, response, body) => {
  if (error)
    console.error(error)
  console.log(response);
})