#!/usr/bin/node
const { argv } = require('node:process');

// return console.log(argv[2]);

if (argv[2] > 0) {
    console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
