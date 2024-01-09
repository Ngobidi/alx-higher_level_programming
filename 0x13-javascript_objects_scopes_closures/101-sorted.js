#!/usr/bin/node
const dictionar = require('./101-data').dictionar;

const totalist = Object.entries(dictionar);
const vals = Object.values(dictionar);
const valsUniq = [...new Set(vals)];
const newdictionar = {};
for (const b in valsUniq) {
  const list = [];
  for (const m in totalist) {
    if (totalist[m][1] === valsUniq[b]) {
      list.unshift(totalist[m][0]);
    }
  }
  newdictionar[valsUniq[b]] = list;
}
console.log(newdictionar);
