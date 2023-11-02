#!/usr/bin/python3

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A class representing a rebel integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.
        """
        return super().__eq__(other)
