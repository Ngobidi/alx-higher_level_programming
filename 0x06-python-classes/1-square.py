#!/usr/bin/python3

"""Define a class Square.
    apply Private instance attribute: size.
"""


class Square:
    """Represents a square from 0-square"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
