#!/usr/bin/python3

""" Module contents  sub class  Mylist inherits from list class."""


class MyList(list):
    """ sub class inherits from list.
    Arg:
        list: a list to sort (ascending sort).
    """

    def print_sorted(self):
        """ Public instance method prints the sorted list(ascending sort).
        """
        mylist = self[:]
        mylist.sort()
        print(mylist)
