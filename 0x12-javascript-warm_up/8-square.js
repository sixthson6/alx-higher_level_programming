#!/usr/bin/node

const num = process.argv[2];

if (process.argv.length < 3) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  console.log('X'.repeat(num));
}
