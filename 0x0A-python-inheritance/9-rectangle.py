#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle with width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Format: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
