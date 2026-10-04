#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    for (const characterUrl of film.characters) {
      if (characterUrl.endsWith(`${characterId}/`)) {
        count += 1;
        break;
      }
    }
  }

  console.log(count);
});
