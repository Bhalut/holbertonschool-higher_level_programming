#!/usr/bin/python3
def no_c(my_string):

    str_new = ""

    for item in my_string:
        if item != "C" and item != "c":
            str_new += item

    return str_new
