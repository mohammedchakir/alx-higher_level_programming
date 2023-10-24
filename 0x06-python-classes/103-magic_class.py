#!/usr/bin/python3
"""writing a docstring"""

import math


class MagicClass:
    """
    This class performs the same operations as the provided Python bytecode.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with an optional radius.

        Args:
            radius (int or float, optional): Radius of circle. Defaults to 0.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
