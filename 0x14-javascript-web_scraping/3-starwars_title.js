#!/usr/bin/node
const movie = process.argv[2];
const axios = require('axios');

const address = 'https://swapi-api.hbtn.io/api/films/' + movie;
axios.get(address)
  .then(function (response) {
    console.log(response.data.title);
  });
