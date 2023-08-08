#!/usr/bin/env python3
def pow(a, b):
    base = a
    if b > 0:
        for i in range(b - 1):
            a = base * a
    elif b == 0:
        a = 1
    else:
        b = b * -1
        for j in range(b - 1):
            a = base * a
        a = 1 / a
    return a
