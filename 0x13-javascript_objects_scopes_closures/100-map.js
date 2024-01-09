#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (n, base) {
  return n * base;
});

console.log(list);
console.log(newList);
