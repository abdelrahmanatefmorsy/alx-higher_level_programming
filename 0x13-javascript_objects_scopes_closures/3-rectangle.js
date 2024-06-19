#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = this.width;
    let str = '';
    while (i > 0) {
      str += 'X';
      i--;
    }
    let j = this.height;
    while (j > 0) {
      console.log(str);
      j--;
    }
  }
};
