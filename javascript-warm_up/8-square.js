#!/usr/bin/node
const { argv } = require('node:process');
if (Number.isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= Number(argv[2]); i++) {
    let side = '';
    let count = 1;
    while (count <= Number(argv[2])) {
      side += 'X';
      count++;
    }
      console.log(side);
  }
}
