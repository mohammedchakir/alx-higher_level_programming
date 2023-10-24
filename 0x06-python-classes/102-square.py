#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """
    This class defines a square with a private instance attribute 'size'.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Equal comparison for square area.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal comparison for square area.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison for square area.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if area is less than the other's area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison for square area.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if area is less than or equal to other's area, False OW.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison for square area.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if area is greater than other's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison for square area.

        Args:
            other (Square): The other Square to compare with.

        Returns:
            bool: True if area is greater than or equal to other's area, F OW.
        """
        return self.area() >= other.area()
