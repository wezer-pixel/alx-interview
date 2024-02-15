#!/usr/bin/node

/**
 * Fetches and prints the names of the characters in a Star Wars film.
 * @param {number} filmId - The ID of the Star Wars film.
 */
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

/**
 * Recursively fetches and prints the names of the characters in the exact order.
 * @param {string[]} actors - The URLs of the characters.
 * @param {number} x - The index of the current character.
 */
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
