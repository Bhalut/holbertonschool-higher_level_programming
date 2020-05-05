#!/usr/bin/python3
def max_integer(my_list=[]):
    maximun = -9999

    if my_list == []:
        return None
    else:
        for num in my_list:
            if num > maximun:
                maximun = num

    return maximun
