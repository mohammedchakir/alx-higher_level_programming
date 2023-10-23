#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """
    Safely prints an integer.

    Args:
        value: The value to be printed.

    Returns:
        True if the value is an integer and has been printed successfully.
        False if value is not an integer, and error msg is printed to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: Not an integer", file=stderr)
        return False
