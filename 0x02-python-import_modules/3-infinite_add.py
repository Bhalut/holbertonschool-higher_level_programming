#!/usr/bin/python3
def add(amount, arg):
    result = 0

    if amount > 1:
        for i in range(1, amount):
            result += int(arg[i])

    return result

if __name__ == "__main__":
    from sys import argv
    print("{:d}".format(add(len(argv), argv)))
