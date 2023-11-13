#!/usr/bin/python3
"""Study a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """display a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """set-up a new_Rectangle.
        Args:
            width (int): w of the new_Rectangle.
            height (int): h of the new_Rectangle.
            x (int): The x co-ordinate of the new-Rectangle.
            y (int): The y co-ordinate of the new-Rectangle.
            id (int): The i.dentity of the new-Rectangle.
        Raises:
            TypeError: when w or h is not an int.
            ValueError: when w or h <= 0.
            TypeError: when x or y is not an int.
            ValueError: when x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """evaluates the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """evaluates the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """evaluates the x co-ordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """evaluates the y co-ordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """compute the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """display the updated Rectangle.
        Args:
            *args (ints): New attribute_values.
                - 1st argument reps i.d_attribute
                - 2nd argument reps width_attribute
                - 3rd argument reps height_attribute
                - 4th argument reps x_attribute
                - 5th argument reps y_attribute
            **kwargs (dict): New key and value pair of attribute.
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.width = arg
                elif b == 2:
                    self.height = arg
                elif b == 3:
                    self.x = arg
                elif b == 4:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for k, u in kwargs.items():
                if k == "id":
                    if u is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = u
                elif k == "width":
                    self.width = u
                elif k == "height":
                    self.height = u
                elif k == "x":
                    self.x = u
                elif k == "y":
                    self.y = u

    def to_dictionary(self):
        """display the dicts reps of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Result the print() and str() reps of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
