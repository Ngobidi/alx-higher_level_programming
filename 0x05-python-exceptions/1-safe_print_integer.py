#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        true - if value is integral, and printed correctly,
        else - false
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
