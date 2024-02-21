#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
const characterId = '18';

request(arg, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (let res = 0; res < data.length - 1; res++) {
      if (data[res].characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});
