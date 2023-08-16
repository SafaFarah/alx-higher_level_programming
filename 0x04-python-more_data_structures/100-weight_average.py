#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    weight = 0
    score = 0
    for i in my_list:
        weight = weight + i[1]
        score = score + (i[0] * i[1])
    return score / weight
