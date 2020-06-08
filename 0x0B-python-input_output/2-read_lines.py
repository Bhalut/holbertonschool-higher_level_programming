#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(file=filename, mode="r", encoding="utf8") as f:
        if nb_lines is not 0:
            for line in range(nb_lines):
                print(f.readline(), end="")
        else:
            for line in f:
                print(line, end="")
