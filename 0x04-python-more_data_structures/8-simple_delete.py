#!/usr/bin/python3
def simple_delete(a_dictio, key=""):
    if key in a_dictio:
        del a_dictio[key]
    return a_dictio
