#!/usr/bin/python3


def magic_calculation(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. c
    """
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(a, b))
