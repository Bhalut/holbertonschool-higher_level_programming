#!/usr/bin/python3
""" 3-is_kind_of_class.py

    is_kind_of_class func
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class func

     returns True if the object is an instance of,
     or if the object is an instance of a class that inherited from,
     the specified class ; otherwise False.

    Args:
        obj (Any): object
        a_class (Any): class

    Returns:
        Boolean: True or False
    """
    if not isinstance(obj, a_class):
        return False

    return True
