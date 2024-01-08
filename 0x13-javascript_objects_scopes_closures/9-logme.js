#!/usr/bin/node

let count = 0; // Variable to keep track of the number of calls to logMe

/**
 * Prints the number of arguments already printed and the new argument value.
 *
 * @param {*} item - The current argument to be printed.
 */
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
