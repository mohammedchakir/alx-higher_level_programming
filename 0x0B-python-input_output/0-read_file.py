#!/usr/bin/python3

"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Note:
        - This function does not handle file permission or not found exceptions
        - It reads the file line by line and prints its contents.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
