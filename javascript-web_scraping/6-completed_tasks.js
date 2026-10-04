#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const tasks = JSON.parse(body);
  const completedByUser = {};

  for (const task of tasks) {
    if (task.completed === true) {
      completedByUser[task.userId] = (completedByUser[task.userId] || 0) + 1;
    }
  }

  console.log(completedByUser);
});
