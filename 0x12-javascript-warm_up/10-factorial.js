#!/usr/bin/node
// calcs a factorial

function fact (a) {
  if (typeof a === 'number' && a >= 0) {
    if (a <= 1) {
      return (1);
    } else {
      return (a * fact(a - 1));
    }
  } else {
    return (1);
  }
}

const number = parseInt(process.argv[2]);

console.log(fact(number));
