#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  /**
     * Prints the square using the specified character.
     *
     * @param {string} c - The character to use for printing the square.
     */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
