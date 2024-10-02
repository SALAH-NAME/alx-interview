#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, async (error, res, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (error, res, body) => {
        if (error) {
          reject(error);
          return;
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
