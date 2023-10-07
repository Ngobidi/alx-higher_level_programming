#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Cut the tuple to the first 2 elements, if lengthy
    # Extend the tuple to match length 2, if very short
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    c = [p + q for p, q in zip(a, b)]
    return tuple(c[0:2])
