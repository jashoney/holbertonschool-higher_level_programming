#!/usr/bin/node
const movieurl = process.argv[2];
const axios = require('axios');

let movies = 0;
let count = 0;

axios.get(movieurl)
  .then(function (response) {
    movies = response.data.results;
    for (const movie in movies) {
      const characters = movies[movie].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }).catch(function (error) {
    console.log(error);
  });
