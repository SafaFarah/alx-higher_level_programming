#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.length - 1;
  for (let i = 0; i < list.length / 2; i++) {
    [list[i], list[j]] = [list[j], list[i]];
    j--;
  }
  return (list);
};
