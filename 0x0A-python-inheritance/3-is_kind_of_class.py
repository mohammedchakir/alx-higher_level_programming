#!/usr/bin/python3

"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it's an instance of a class
    that inherited from, the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class or its subclass,
    otherwise False.
    """
    return isinstance(obj, a_class)
