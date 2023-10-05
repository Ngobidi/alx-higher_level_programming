#!/usr/bin/python3
import hidden_4


def discovr():
    name = dir(hidden_4)
    for z in name:
        if z[:2] != '__':
            print("{:s}".format(z))


if __name__ == "__main__":
    discovr()
