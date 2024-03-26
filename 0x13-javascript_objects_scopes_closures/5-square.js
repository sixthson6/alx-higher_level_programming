#!/usr/bin/node
//Create square class
//Inherit from Rectangle class
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
	constructor(size) {
		super(size, size);
	}
}
