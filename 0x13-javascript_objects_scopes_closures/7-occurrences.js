#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let frq = 0;
  while (i < list.length) {
    if (list[i] === searchElement) { frq++; }
    i++;
  }
  return frq;
};
