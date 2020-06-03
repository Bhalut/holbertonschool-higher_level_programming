#!/usr/bin/python3
""" 4-inherits_from.py

    inherints_from func
"""


def inherits_from(obj, a_class):
    """inherits_from func

     returns True if the object is an instance of a class
     that inherited (directly or indirectly)
     from the specified class ; otherwise False.

    Args:
        obj (Any): object
        a_class (Any): class

    Returns:
        Boolean: True or False
    """
    if not isinstance(obj, a_class):
        return False

    return True
