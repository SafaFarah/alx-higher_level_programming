#!/usr/bin/node
const dict = require('./101-data').dict;
const list = Object.entries(dict);
const swap = list.map(([key, value]) => [value, key]);
console.log(Object.fromEntries(swap));
