#!/usr/bin/python3
"""compute a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """display a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """set-up a new_Square.
        Args:
            size (int): new_Square size.
            x (int): x co-ordinate of the new_Square.
            y (int): y co-ordinate of the new_Square.
            id (int): i.dentity of the new_Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """evaluate the Square_size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """compiled square.
        Args:
            *args (ints): New attributes value.
                - 1st argument reps id_attribute
                - 2nd argument reps size_attribute
                - 3rd argument reps x_attribute
                - 4th argument reps y_attribute
            **kwargs (dict): New keys and values pair of attribute.
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.size = arg
                elif b == 2:
                    self.x = arg
                elif b == 3:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for k, u in kwargs.items():
                if k == "id":
                    if u is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = u
                elif k == "size":
                    self.size = u
                elif k == "x":
                    self.x = u
                elif k == "y":
                    self.y = u

    def to_dictionary(self):
        """outline the dict reps of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and string() reps of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
