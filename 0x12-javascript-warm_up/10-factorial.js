#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num1 = parseInt(args[2]);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const fact = factorial(num1);
console.log(fact);
