#!/usr/bin/node
/* compute factorial */
function calcFactorial (num) {
  if (isNaN(num)) {
    return 1;
  }
  let res;
  if (num === 0) {
    return 1;
  } else {
    return num * calcFactorial(num - 1);
  }
}

const num = parseInt(process.argv[2]);
const res = calcFactorial(num);

console.log(res)
