#!/usr/bin/python3
""" 1-my_list.py

    MyList Class
"""


class MyList(list):
    """MyList class

    MyList that inherits from list

    Inherence:
        list : list class
    """

    def print_sorted(self):
        """print_sorted func

        print sorted list
        """
        print(sorted(self))
