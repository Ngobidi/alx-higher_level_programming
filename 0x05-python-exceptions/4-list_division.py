#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists elements by elements 2.

    Args:
        my_list_1 (list): The list1.
        my_list_2 (list): The list2.
        list_length (int): The num of elements to be divided.

    Returns:
        New list - (length = list_length) with all divisions
        0 - If 2 elements can’t be divided
    """
    new_list = []
    for j in range(0, list_length):
        try:
            div = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
