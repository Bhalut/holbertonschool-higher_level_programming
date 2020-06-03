#!/usr/bin/python3
""" 0-lookup.py

    lookup function
"""


def lookup(obj):
    """lookup func

    returns the list of available attributes and methods of an object

    Args:
        obj (Any): Object

    Returns:
        list: list object
    """
    return dir(obj)
