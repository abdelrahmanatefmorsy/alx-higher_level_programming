#!/usr/bin/node
const varone = process.argv[2];
const vartwo = process.argv[3];
function add (a, b) {
  if (isNaN(a) || isNaN(b)) { console.log('NaN'); } else { console.log(Number(a) + Number(b)); }
}
add(varone, vartwo);
