#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios');
const fs = require('fs');
const file = process.argv[3];

let data = '';

axios.get(url)
  .then(function (response) {
    data = response.data;
    fs.writeFile(file, data, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  });
