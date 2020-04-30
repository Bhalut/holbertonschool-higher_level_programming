#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arg = sys.argv

if len(arg) is 2:
    print("{:d} argument.".format(len(arg) - 1))
    print("{:d}: {}".format(len(arg) - 1, arg[len(arg) - 1]))
elif len(arg) > 2:
    print("{:d} arguments:".format(len(arg) - 1))
    for index in range(1, len(arg)):
        print("{:d}: {}".format(index, arg[index]))
else:
    print("{:d} arguments.".format(len(arg) - 1))
