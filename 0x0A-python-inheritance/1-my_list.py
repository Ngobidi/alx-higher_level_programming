#!/usr/bin/python3
"""
contains the MyList class
print the lists sorted in ascending order.
"""


class MyList(list):
    """a sub_class of list"""
    def __init__(self):
        """set_up the objects"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted lists in ascending order"""
        print(sorted(self))
