#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    y = len(argv) - 1
    if y != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if op == '+':
