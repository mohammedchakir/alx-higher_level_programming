#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
