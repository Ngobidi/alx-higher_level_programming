#!/usr/bin/python3

if __name__ == "__main__":
    """Print the summation of all argument."""
    import sys

    result = 0
    for z in range(len(sys.argv) - 1):
        result += int(sys.argv[z + 1])
