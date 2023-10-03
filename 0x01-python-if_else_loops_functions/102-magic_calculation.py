#!/usr/bin/python3
def magic_calculation(e, f, g):
    if e < f:
        return g
    if g > f:
        return e + f
    return e * f - g
