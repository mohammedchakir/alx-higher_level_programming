#!/usr/bin/node

/**
 * Returns a function that converts a number from base 10 to a specified base.
 *
 * @param {number} base - The base to convert to.
 * @return {Function} A converter function.
 */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
