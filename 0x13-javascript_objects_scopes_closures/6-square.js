#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    let i = 0;
    let j = 0;
    let str = '';
    while (i < this.width) {
      str += c;
      i++;
    }
    while (j < this.height) {
      console.log(str);
      j++;
    }
  }
};
