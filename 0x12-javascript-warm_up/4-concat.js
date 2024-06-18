#!/usr/bin/node
let varone = process.argv[2];
let vartwo = process.argv[3];
if (varone === undefined) { varone = 'undefined'; }
if (vartwo === undefined) { vartwo = 'undefined'; }
console.log(varone, ' is ', vartwo);
