#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    n = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for s in range(len(roman_string)):
        if roman_string[s] not in list(roman.keys()):
            return None
        else:
            if s > 0 and roman[roman_string[s]] > roman[roman_string[s - 1]]:
                n = n + roman[roman_string[s]] - 2 * roman[roman_string[s - 1]]
            else:
                n = n + roman[roman_string[s]]
    return n
