#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an int with "{:d}".format().
    Args:
        value (int): The integers to print.
    Returns:
        true - if  if value (integers) has been correctly printed.
        else false False and prints in stderr followed by Exception.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
