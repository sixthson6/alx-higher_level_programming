#!/usr/bin/node

const myNum = process.argv[2];

if (!isNaN(myNum) && Number.isInteger(Number(myNum))) {
  console.log(`My number: ${parseInt(myNum)}`);
} else if (!isNaN(myNum) && myNum % 1 !== 0) {
  console.log(`My number: ${parseFloat(myNum)}`);
} else {
  console.log('Not a number');
}
