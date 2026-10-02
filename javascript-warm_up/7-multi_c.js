#!/usr/bin/node
const { argv } = require('node:process');
if (Number.isNaN(Number(argv[2]))) {
  console.log('Missing number of occurances');
} else {
  for (let i = 1; i <= Number(argv[2]); i++) {
    console.log('C is fun');
  }
}
