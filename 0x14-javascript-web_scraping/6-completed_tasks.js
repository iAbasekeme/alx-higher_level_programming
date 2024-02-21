#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const emptyObject = {};
  for (let dat = 0; dat < data.length; dat++) {
    if (data[dat].completed) {
      emptyObject[data[dat].userId] = (emptyObject[data[dat].userId] || 0) + 1;
    }
  }
  console.log(emptyObject);
});
