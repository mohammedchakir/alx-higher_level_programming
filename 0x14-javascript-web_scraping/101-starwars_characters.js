#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  charactersUrls.reduce((prev, characterUrl) => {
    return prev.then(() => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
            reject(error);
            return;
          }
          const character = JSON.parse(body);
          console.log(character.name);
          resolve();
        });
      });
    });
  }, Promise.resolve());
});
