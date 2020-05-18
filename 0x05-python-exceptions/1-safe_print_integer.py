#!/usr/bin/python3
def safe_print_integer(value):
    isInteger = True
    try:
        print("{:d}".format(value))
    except ValueError:
        isInteger = False

    return isInteger
