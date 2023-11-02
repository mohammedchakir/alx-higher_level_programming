#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A base geometry class with an area method that raises an exception.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")
