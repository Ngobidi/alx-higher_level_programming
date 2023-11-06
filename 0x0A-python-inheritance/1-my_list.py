#!/usr/bin/python3
"""
define MyList class
"""


class MyList(list):
    """print a subclass of list"""
    def __init__(self):
        """set-up the obj"""
        super().__init__()

    def print_sorted(self):
        """display the sorted list in asending order"""
        print(sorted(self))
