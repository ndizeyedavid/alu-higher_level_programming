#!/usr/bin/node
const { argv } = require('node:process');
if (Number.isNaN(Number(argv[2])) && Number.isNaN(Number(argv[3]))) {
  console.log('Missing Numbers');
} else {
  console.log(Number(argv[2]) + Number(argv[3]));
}
