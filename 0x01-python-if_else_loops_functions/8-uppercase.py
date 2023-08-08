#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n > 96 and n < 123:
            n = n - 32
        c = chr(n)
        print('{}'.format(c), end='')
    print()
