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
  let largest = arr[0];
  let largest2 = -Infinity;
  for (let j = 1; j < arr.length; j++) {
    if (arr[j] > largest) {
      largest2 = largest;
      largest = arr[j];
    } else if (arr[j] < largest && arr[j] > largest2) {
      largest2 = arr[j];
    }
  }
  console.log(largest2);
}
