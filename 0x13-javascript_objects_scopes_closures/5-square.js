#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /**
     * Creates an instance of Square.
     *
     * @param {number} size - The size of the square.
     */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
