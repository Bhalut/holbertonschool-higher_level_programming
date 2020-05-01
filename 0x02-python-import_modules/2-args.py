#!/usr/bin/python3
def printArg(amount, arg):
    if amount is 2:
        print("{:d} argument:".format(amount - 1))
        print("{:d}: {}".format(amount - 1, arg[amount - 1]))
    elif len(arg) > 2:
        print("{:d} arguments:".format(amount - 1))
        for index in range(1, amount):
            print("{:d}: {}".format(index, arg[index]))
    else:
        print("{:d} arguments.".format(amount - 1))

if __name__ == "__main__":
    from sys import argv
    printArg(len(argv), argv)
