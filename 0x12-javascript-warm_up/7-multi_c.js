#!/usr/bin/node
// prints argv1 dependant on the number of args passed

const myLine = 'C is fun';

const j = parseInt(process.argv[2]);

if (process.argv.length >= 3 && (j)) {
  for (let i = 0; i < j; i++) {
    console.log(myLine);
  }
} else {
  console.log('Missing number of occurrences');
}
