#!/usr/bin/node

function add (a, b) {
  a = Number(process.argv[2]);
  b = Number(process.argv[3]);
  const res = a + b;
  console.log(res);
}

add();
