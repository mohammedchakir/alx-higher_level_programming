#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle.
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

        :param size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
