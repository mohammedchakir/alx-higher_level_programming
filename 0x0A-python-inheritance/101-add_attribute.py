#!/usr/bin/python3

"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    :param obj: The object to which the attribute should be added.
    :param attr_name: The name of the attribute.
    :param attr_value: The value of the attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
