#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        x = length(my_list)
    finally:
        print("")

    return my_list[x - 1]


def length(my_list=[]):
    count = 0
    for i in my_list:
        count += 1

    return count
