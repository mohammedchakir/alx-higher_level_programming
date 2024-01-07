#!/usr/bin/node

/**
 * Counts the number of occurrences of a given element in a list.
 *
 * @param {Array} list - The array to search through.
 * @param {*} searchElement - The element to count occurrences of.
 * @return {number} The number of occurrences of the search element.
 */
exports.nbOccurences = function (list, searchElement) {
    return list.filter(element => element === searchElement).length;
};
