#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unqi = set(my_list)
    for i in unqi:
        sum = sum + i
    return sum
