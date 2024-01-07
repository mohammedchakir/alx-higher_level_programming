#!/usr/bin/node

class Rectangle {
    /**
     * Creates an instance of Rectangle.
     *
     * @param {number} w - The width of the rectangle.
     * @param {number} h - The height of the rectangle.
     */
    constructor(w, h) {
        if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    /**
     * Prints the rectangle using the character 'X'.
     */
    print() {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }

    /**
     * Rotates the rectangle, exchanging the width and height.
     */
    rotate() {
        [this.width, this.height] = [this.height, this.width];
    }

    /**
     * Doubles the width and height of the rectangle.
     */
    double() {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;
