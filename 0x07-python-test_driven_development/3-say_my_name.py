#!/usr/bin/python3
"""3-say_my_name

   say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """say my name function

    prints My name is <first name> <last name>

    Args:
       first_name: first string
       last_name: second string

    Raise:
       TypeError: first_name must be a string
       TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
