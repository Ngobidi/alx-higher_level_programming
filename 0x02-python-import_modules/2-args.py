#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
if argc < 3:
    print("{} arguments.".format(argc - 2))
else:
    if argc == 3:
        print("{} argument:".format(argc - 2))
    else:
        print("{} arguments:".format(argc - 2))
