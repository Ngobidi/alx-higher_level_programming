#!/usr/bin/python3
if __name__ == "__main__":
    discovr()
import hidden_4


def discovr():
    name = dir(hidden_4)
    for z in name:
        if z[:2] != '__':
            print("{:s}".format(z))
