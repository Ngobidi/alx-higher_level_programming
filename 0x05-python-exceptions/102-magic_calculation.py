#!/usr/bin/python3
def magic_calculation(a, b):
    ref = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            ref += a ** b / j
        except Exception:
            ref = b + a
            break
    return ref
