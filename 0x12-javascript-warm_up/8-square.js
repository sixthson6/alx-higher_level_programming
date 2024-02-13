#!/usr/bin/node

const num = process.argv[2];

if (process.argv.length < 3 && !(Number.isInteger(Number(num))) && Number(num) === num) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
