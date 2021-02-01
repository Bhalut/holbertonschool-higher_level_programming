#!/usr/bin/python3
""" 6-peak

    function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Function max integer

    Args:
        list_of_integers (list)

    Returns:
        Max integer or None
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
