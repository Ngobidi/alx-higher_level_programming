#!/usr/bin/python3
def remove_char_at(str, m):
    t = ""
    for j in range(len(str)):
        if j != m:
            t = t + str[j]
    return (t)
