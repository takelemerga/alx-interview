#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie
 */

const request = require('request');
const movieID = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films';

execute(movieID);

async function execute (movieID) {
  const prom = await makeRequest(`${url}/${movieID}`);
  for (const ch of prom.characters) {
    const e = await makeRequest(ch);
    console.log(e.name);
  }
}

function makeRequest (location) {
  return new Promise(function (resolve, reject) {
    request(location, (error, res, body) => {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}
