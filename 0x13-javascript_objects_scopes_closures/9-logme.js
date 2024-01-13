#!/usr/bin/node

let i = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(`${i}: ${item}`);
    i++;
  }
};
