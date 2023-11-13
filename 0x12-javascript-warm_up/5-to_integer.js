#!/usr/bin/node
let number;
number = parseInt(process.argv[2]);
if (!isNaN(number)) {
  const string = 'My number: ' + number;
  console.log(string);
} else {
  console.log('Not a number');
}
