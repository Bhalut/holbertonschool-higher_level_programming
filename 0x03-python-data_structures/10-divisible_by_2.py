#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = list()

    if my_list:
        for item in my_list:
            if item % 2 == 0:
                result.append(True)
            else:
                result.append(False)

    return result
