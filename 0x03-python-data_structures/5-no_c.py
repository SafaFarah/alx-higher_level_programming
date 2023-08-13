#!/usr/bin/env python3
def no_c(my_string):
    if my_string is not None:
        s_list = list(my_string)
        for ch in s_list:
            if ch == 'c' or ch == 'C':
                s_list.remove(ch)
    return("".join(s_list))
