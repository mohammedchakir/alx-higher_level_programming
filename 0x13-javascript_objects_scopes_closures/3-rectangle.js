#!/usr/bin/node

class Rectangle {
  /**
     * Creates an instance of Rectangle.
     *
     * @param {number} w - The width of the rectangle.
     * @param {number} h - The height of the rectangle.
     */
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
     * Prints the rectangle using the character 'X'.
     */
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
