#!/usr/bin/node
let myVar = process.argv[2];
if (isNaN(myVar)) { console.log('Missing size'); } else {
  let strr = '';
  let i = 0;
  while (i < myVar) {
    strr += 'X';
    i++;
  }
  while (myVar > 0) {
    console.log(strr);
    myVar = myVar - 1;
  }
}
