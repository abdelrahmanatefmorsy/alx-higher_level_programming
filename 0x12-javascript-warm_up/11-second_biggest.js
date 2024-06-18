#!/usr/bin/node
let i = 2;
let mx1 = 0;
let mx2 = 0;
while (i < process.argv.length) {
  const num = Number(process.argv[i]);
  if (num >= mx1) {
    mx2 = mx1;
    mx1 = num;
  } else if (num >= mx2) {
    mx2 = num;
  }
  i++;
}
console.log(mx2);
