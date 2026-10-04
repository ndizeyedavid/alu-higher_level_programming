#!/usr/bin/node
const OSquare = require('./5-square');
class Square extends OSquare {
  charPrint (letter) {
    for (let i = 0; i < this.width; i++) {
      let result = '';
      for (let y = 0; y < this.width; y++) {
        result += letter || 'X';
      }
      console.log(result);
    }
  }
}
module.exports = Square;
