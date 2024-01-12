#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
      return {};
    }
  }
}
module.exports = Rectangle;
