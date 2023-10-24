#!/usr/bin/python3

"""Define a class Square.
    applied Private instance attribute: size
    size must be an integers.
    else TypeError
"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new_square.

        Args:
            size (int): The size of the new_square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
