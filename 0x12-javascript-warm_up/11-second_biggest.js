#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < args.length; i++) {
    arr.push(parseInt(args[i]));
  }
  arr.sort();
  arr.reverse();
  for (let j = 1; j < arr.length; j++) {
    if (arr[j] !== arr[0]) {
      console.log(arr[j]);
      break;
    }
  }
}
