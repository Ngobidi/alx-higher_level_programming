#!/usr/bin/python3

"""Define a class Square from new_square.
    apply Private instance attribute: size
    size must be an integers.
    size must be >= 0.
    else TypeError or ValueError
"""


class Square:
    """Represent a square from new_square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
