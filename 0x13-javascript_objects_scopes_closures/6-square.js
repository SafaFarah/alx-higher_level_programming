#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row = row + c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
};
