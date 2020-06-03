#!/usr/bin/python3
def add_attribute(obj, attr, value):
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
