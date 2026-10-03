#!/usr/bin/node
const { argv } = require('node:process');
const numbers = [];
argv.forEach((val, index) => {
  if (Number.isNaN(Number(val))) {
    numbers.push(0);
  } else {
    numbers.push(Number(val));
  }
});
if (numbers.length > 2) {
  console.log(numbers.sort((a, b) => b - a)[1]);
} else {
  console.log(0);
}
