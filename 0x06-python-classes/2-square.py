#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """
    This class defines a square with a private instance attribute 'size'.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
