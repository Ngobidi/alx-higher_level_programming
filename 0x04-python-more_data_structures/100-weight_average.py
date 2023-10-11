#!/usr/bin/python3
def weight_average(my_list=[]):
    """
     fn that returns the average weight
     of all integers tuple
    """
    if not my_list:
        return 0

    number = 0
    mass = 0

    for tup in my_list:
        number += tup[0] * tup[1]
        mass += tup[1]

    return (number / mass)
