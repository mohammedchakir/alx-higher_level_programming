#!/usr/bin/node

/**
 * Returns the reversed version of a list.
 *
 * @param {Array} list - The array to be reversed.
 * @return {Array} A new array with elements in the reverse order.
 */
exports.esrever = function (list) {
    let reversedList = [];
    for (let i = list.length - 1; i >= 0; i--) {
        reversedList.push(list[i]);
    }
    return reversedList;
};
