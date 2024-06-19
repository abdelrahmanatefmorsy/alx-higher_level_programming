#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
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
