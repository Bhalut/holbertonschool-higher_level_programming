#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        x = length(my_list)
    finally:
        print("")

    return count


def length(my_list=[]):
    count = 0
    for i in my_list:
        count += 1

    return count
