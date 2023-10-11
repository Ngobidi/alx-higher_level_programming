#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    for new in sorted(my_dictionary.keys()):
        print("{}: {}".format(new, my_dictionary[new]))
