#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  if (list) {
    const storage = [];
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        storage.push(i);
      }
    }
    return storage.length;
  } else {
    return 0;
  }
}
