#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    keys = list(a_dictionary.keys())
    best = keys[0]
    for i in range(1, len(keys)):
        if a_dictionary[keys[i]] > a_dictionary[best]:
            best = keys[i]
    return best
