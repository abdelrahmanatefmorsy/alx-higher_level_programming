#!/usr/bin/node
const varone = process.argv[2];
function factorial (a) {
  a = parseInt(a);
  if (a === 1 || isNaN(a)) { return 1; }
  return factorial(a - 1) * a;
}
console.log(factorial(varone));
