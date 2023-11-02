#!/usr/bin/python3

"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
