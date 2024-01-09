#!/usr/bin/node
let logNo = 0;
exports.logMe = function (item) {
  console.log((logNo++) + ': ' + item);
};
