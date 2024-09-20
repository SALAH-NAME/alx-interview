#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(apiUrl, function (err, res, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  printCharactersInOrder(characters, 0);
});

const printCharactersInOrder = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printCharactersInOrder(characters, index + 1);
  });
};
