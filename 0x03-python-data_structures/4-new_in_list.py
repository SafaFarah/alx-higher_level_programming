#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = []
    for n in my_list:
        copy_list.append(n)
    if idx < 0:
        return copy_list
    if idx > len(copy_list) - 1:
        return copy_list
    for i in range(len(copy_list)):
        if i == idx:
            copy_list[i] = element
    return copy_list
