#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1;
  let a = 0;
  while ((length - a) > 0) {
    const aux = list[length];
    list[length] = list[a];
    list[a] = aux;
    a++;
    length--;
  }
  return list;
};
