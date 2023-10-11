#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = [data[x] for x in roman_string] + [0]
    result = 0

    for x in range(len(numbers) - 1):
        if n[x] >= n[x+1]:
            result += n[x]
        else:
            result -= n[x]

    return result
