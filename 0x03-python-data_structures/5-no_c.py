#!/usr/bin/env python3
def no_c(my_string):
    if my_string is not None:
        s_list = list(my_string)
        new_list =[]
        for ch in s_list:
            if ch != 'c' and ch != 'C':
                new_list.append(ch)
        new_string = "".join(new_list)
    return new_string
