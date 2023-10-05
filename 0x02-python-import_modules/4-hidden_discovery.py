#!/usr/bin/python3
if __name__ == "__main__":
    import max_4
    for name in dir(max_4):
        if name[0] != '_' and name[1] != '_':
            print(name)
