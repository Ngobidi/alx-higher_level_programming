#!/usr/bin/python3
def print_last_digit(numb):
    if numb >= 0:
        l_digit = numb % 10
    else:
        l_digit = numb % -10
        l_digit *= -1

    print("{:d}".format(l_digit), end='')
    return (l_digit)
