#!/usr/bin/python3
""" 101-add_attribute.py

    add_attribute func
"""


def add_attribute(obj, attr, value):
    """add_attribute func

    adds a new attribute to an object if it’s possible

    Args:
        obj (any): Object
        attr (eny): Attribute
        value (any): value

    Raises:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
