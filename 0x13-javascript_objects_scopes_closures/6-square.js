#!/usr/bin/node

const Square2 = require('./5-square');
class Square extends Square2 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;