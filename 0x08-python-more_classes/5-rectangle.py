#!/usr/bin/python3

"""defines a rectangle class"""


class Rectangle:
    """
    This class defines a rectangle with width and height attributes.
    It includes methods for calculating area, perimeter, and provides
    string representation using the '#' character. It also prints a
    farewell message when an instance is deleted.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle with an optional width and height.
        Default values for width and height are set to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Width must be an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Height must be an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#'.
        If width or height is 0, an empty string is returned.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Return a string representation that can recreate a new instance.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Print a farewell message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
