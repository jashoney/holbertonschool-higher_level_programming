#!/usr/bin/node
// prints argv1 dependant on the number of args passed

const arg2 = process.argv[2];
const arg3 = process.argv[3];

if (arg3) {
  const sentence = arg2 + ' is ' + arg3;
  console.log(sentence);
} else if (arg2) {
  const sentence = arg2 + ' is undefined';
  console.log(sentence);
} else {
  console.log('undefined is undefined');
}
