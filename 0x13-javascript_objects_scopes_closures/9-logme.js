#!/usr/bin/node
// returns a count of a search element inside a list

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
