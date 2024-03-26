#!/usr/bin/node
// Square class
const Squared = require('./5-square');

module.exports = class Square extends Squared {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log('c'.repeat(this.height));
    }
  }
};
