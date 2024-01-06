#!/usr/bin/node

class Rectangle {
    /**
     * Creates an instance of Rectangle.
     *
     * @param {number} w - The width of the rectangle.
     * @param {number} h - The height of the rectangle.
     */
    constructor(w, h) {
        if (this.isPositiveInteger(w) && this.isPositiveInteger(h)) {
            this.width = w;
            this.height = h;
        }
    }

    /**
     * Checks if a value is a positive integer.
     *
     * @param {number} value - The value to check.
     * @returns {boolean} True if value is a positive integer, false otherwise.
     */
    isPositiveInteger(value) {
        return Number.isInteger(value) && value > 0;
    }
}

module.exports = Rectangle;
