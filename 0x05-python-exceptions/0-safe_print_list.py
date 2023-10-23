#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
        all elements to be printed on same line, then \n.
        x can be bigger than length of my_list
    Returns:
        The number of elements printed.
    """
    ref = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ref += 1
        except IndexError:
            break
    print("")
    return (ref)
