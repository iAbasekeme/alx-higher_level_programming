#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const page = process.argv[2];

request(page, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = response.body;
    fs.writeFile(file, data, 'utf-8', (err) => {
	if (err) {
		console.error(err);
	}
    })
  }
})
