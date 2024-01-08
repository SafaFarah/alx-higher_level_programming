#!/usr/bin/node
const process = require('process');
const args = process.argv;
const number = parseInt(args[2]);
let row;
if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    row = '';
    for (let j = 0; j < number; j++) {
      row = 'X' + row;
    }
    console.log(row);
  }
}
