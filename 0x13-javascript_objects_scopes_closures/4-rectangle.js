#!/usr/bin/node
// Rectangle with arg validation
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.witdth;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.widht * 2;
    this.height = this.height * 2;
  }
};
