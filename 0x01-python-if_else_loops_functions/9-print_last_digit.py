#!/usr/bin/python3
def print_last_digit(number):
    str_num = str(number)
    last_str = str_num[-1]
    last_num = int(last_str)
    print(last_num, end="")
    return last_num
