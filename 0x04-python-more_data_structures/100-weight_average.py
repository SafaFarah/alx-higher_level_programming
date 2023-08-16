#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    weight = 0
    score = 0
    for i in my_list:
        weight = weight + i[1]
        score = score + (i[0] * i[1])
    if weight == 0 and score == 0:
        return 0
    return score / weight
