#!/usr/bin/python3
""" 2-read_lines.py

    read_lines func
"""


def read_lines(filename="", nb_lines=0):
    """read_lines func

    reads n lines of a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): file. Defaults to "".
        nb_lines (int, optional): number of lines. Defaults to 0.
    """
    with open(file=filename, mode="r", encoding="utf8") as f:
        if nb_lines == 0:
            for line in f:
                print(line, end="")

        if nb_lines > 0:
            for line in range(nb_lines):
                print(f.readline(), end="")
