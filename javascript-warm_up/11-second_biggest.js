#!/usr/bin/node
const { argv } = require('node:process');
let numbers = [];
argv.forEach((val, index) => {
  if (Number.isNaN(Number(val))) {
    numbers.push(0);
  } else {
    numbers.push(val);
  }
});
if (numbers.length > 2) {
  console.log(numbers.sort()[numbers.length - 2]);
} else {
  console.log(0);
}
