#!/usr/bin/python3
if __name__ == "__main__":
    import sys

if len(sys.argv) > 1:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for index in range(1, len(sys.argv)):
        print("{:d}: {}".format(index, sys.argv[index]))
else:
    print("{:d} arguments.".format(len(sys.argv) - 1))
