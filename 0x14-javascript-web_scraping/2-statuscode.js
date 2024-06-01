#!/usr/bin/node
const arg = process.argv;
const request = require('request');
request(arg[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else { console.log('code: ', response.statusCode); }
});
