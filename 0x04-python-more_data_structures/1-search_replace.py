#!/usr/bin/python3


def search_replace(my_list, search, replace):

    replace_list = []
    for element in my_list:
        if element == search:
            replace_list.append(replace)
        else:
            replace_list.append(element)
    return replace_list
