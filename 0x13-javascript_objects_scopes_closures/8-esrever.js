#!/usr/bin/node
// returns a count of a search element inside a list

exports.esrever = function (list) {
  const reverse = [];
  for (let i = 0; i < list.length; i++) {
    reverse.push(list[i]);
  }
  return reverse;
};
