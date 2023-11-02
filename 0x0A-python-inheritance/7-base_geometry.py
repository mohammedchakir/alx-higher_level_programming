#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A base geometry class with methods to validate and calculate area.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer and greater than 0.

        :param name: A string representing the name of the value.
        :param value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
