#!/usr/bin/node
const { argv } = require('node:process');
function factorial(num) {
  if (num == 1 || Number.isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(Number(argv[2])));
