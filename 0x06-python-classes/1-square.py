#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """
    This class defines a square with a private instance attribute 'size'.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
