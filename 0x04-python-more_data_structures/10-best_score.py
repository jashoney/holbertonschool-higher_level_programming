#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    most = 0
    vlist = a_dictionary.values()
    i = 0
    for v in vlist:
        if v > most:
            most = v
            j = i
        i = i + 1
    keys = list(a_dictionary.keys())
    return (keys[j])
