#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
fs.readFile(arg[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
