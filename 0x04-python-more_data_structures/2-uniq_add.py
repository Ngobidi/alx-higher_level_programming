#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    function that adds all
    unique integers in a list
    """
    add_unique_list = set(my_list)
    value = 0

    for z in add_unique_list:
        value += z

    return (value)
