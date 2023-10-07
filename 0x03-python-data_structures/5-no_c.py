#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for z in my_string:
        if z != 'c' and z != 'C':
            new_string += z
    return new_string

