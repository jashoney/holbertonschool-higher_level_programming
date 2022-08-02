#!/usr/bin/node
// converts a number number to a base

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
