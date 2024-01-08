#!/usr/bin/node
const process = require('process');
const args = process.argv;
const number = parseInt(args[2]);
if (!number) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
