#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b.
    division result to be printed on finally,then by inside result
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
