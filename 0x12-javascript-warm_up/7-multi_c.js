#!/usr/bin/node

const msg = 'C is fun';
const num = process.argv[2];

if (!isNaN(num)) {
  for (let i = 1; i <= num; i++) {
    console.log(msg);
  }
} else {
  console.log('Missing number of occurrences');
}
