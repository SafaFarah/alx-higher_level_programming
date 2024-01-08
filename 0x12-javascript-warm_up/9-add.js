#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(num1, num2);
