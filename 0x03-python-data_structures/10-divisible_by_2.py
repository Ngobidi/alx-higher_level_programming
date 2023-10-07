#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    develop_list = [n % 2 == 0 for n in my_list]

    return develop_list
