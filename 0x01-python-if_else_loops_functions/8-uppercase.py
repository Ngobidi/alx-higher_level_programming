#!/usr/bin/python3
def uppercase(str):
    for z in range(len(str)):
        if ord(str[z]) >= 97 and ord(str[z]) <= 122:
            numb = 32
        else:
            numb = 0
        print("{:c}".format(ord(str[z]) - numb), end='')
    print()
