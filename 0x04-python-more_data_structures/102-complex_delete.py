#!/usr/bin/python3
def complex_delete(a_dictio, value):
    list_keys = list(a_dictio.keys())

    for result in list_keys:
        if value == a_dictio.get(result):
            del a_dictio[result]

    return (a_dictio)
