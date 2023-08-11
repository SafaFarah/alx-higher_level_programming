#!/usr/bin/python3
from sys import argv


def main():
    pass


if __name__ == '__main__':
    n = len(argv)
    if n == 1:
        print("{} arguments.".format(n - 1))
    elif n == 2:
        print("{0} argument:\n{0}: {1}".format((n - 1), argv[n - 1]))
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{0}: {1}".format(i, argv[i]))
    main()
