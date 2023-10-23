#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are int.
    Args:
        my_list (list): The list of element to be printed
        x (int): The num of elements of my_list to be printed.
        other type of value to be skipped
    Returns:
        The num of element printed.
    """
    ref = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            ref += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ref)
