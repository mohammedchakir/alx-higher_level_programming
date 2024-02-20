#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

let count = 0;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
