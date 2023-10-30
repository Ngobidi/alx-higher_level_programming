#!/usr/bin/python3
"""define a method for working with rectangles.
"""


class Rectangle:
    """Represents a rectangle shape class.
    """
    num_of_instances = 0

    def __init__(self, width=0, height=0):
        """set-up a Rectangle with a defined width and height.
        Args:
            width (int): The width_rectangle.
            height (int): The height_rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.num_of_instances += 1

    @property
    def width(self):
        """cal the width of the Rectangle.
        Returns:
            int: The width_Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """cal the height of the Rectangle.
        Returns:
            int: The height_Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """display the width of this Rectangle.
        Args:
            value (int): The new_width of the Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """display the height of the Rectangle.
        Args:
            value (int): The new_height of the Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """evaluate the area of the Rectangle.
        Returns:
            int: The area_Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """evaluate the perimeter of this Rectangle.
        Returns:
            int: The perimeter_Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Result a str representation of this Rectangle.
        Returns:
            str: A str representation of this Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            result = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(result)

    def __repr__(self):
        """Result a representation of the Rectangle's set-up.
        Returns:
            str: A str representation of this Rectangle's set-up.
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """stimulates some routine after an object its delete.
        """
        print('Bye rectangle...')
        Rectangle.num_of_instances -= 1
