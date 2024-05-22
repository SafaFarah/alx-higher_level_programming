#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
fs.writeFile(arg[2], arg[3], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
