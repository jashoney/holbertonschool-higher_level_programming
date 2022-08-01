#!/usr/bin/node
// prints argv1 dependant on the number of args passed

const arg2 = process.argv[2];

if (arg2) {
  console.log(arg2);
} else {
  console.log('No argument');
}
