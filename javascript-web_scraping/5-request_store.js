#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', (writeErr) => {
    if (writeErr) {
      console.log(writeErr);
    }
  });
});
