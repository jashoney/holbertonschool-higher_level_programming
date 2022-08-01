#!/usr/bin/node
// prints argv1 dependant on the number of args passed

const arg2 = process.argv[2];
const number = parseInt(arg2);

if (number) {
  const sentence = 'My number: ' + number;
  console.log(sentence);
} else {
  console.log('Not a number');
}
