#!/usr/bin/node
let myVar = process.argv[2];
if (myVar === undefined) { console.log('Missing number of occurrences'); } else {
  while (myVar > 0) {
    console.log('C is fun');
    myVar = myVar - 1;
  }
}
