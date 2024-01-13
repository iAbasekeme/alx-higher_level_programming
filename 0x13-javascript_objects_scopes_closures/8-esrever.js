#!/usr/bin/node

exports.esrever = function (list) {
  if (list) {
    const storage = [];
    for (let i = list.length - 1; i >= 0; i--) {
      storage.push(list[i]);
    }
    return storage;
  }
};
