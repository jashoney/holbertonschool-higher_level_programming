#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');

const dict = {};
let count = 0

axios.get(url)
  .then(function (response) {
    for (const num in response.data) {
      const id = response.data[num].userId;
      const task = response.data[num].completed;
      if (dict[id] >= 1) {
        count = dict[id];
      } else {
        count = 0;
      }
      if (task) {
        count += 1;
      }
      dict[id] = count;

      if (dict[id] === 0) {
        delete dict[id];
      }
    }
    console.log(dict);
  })
  .catch(function (err) {
    console.error(err);
  });
