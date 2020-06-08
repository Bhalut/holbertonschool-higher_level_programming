#!/usr/bin/python3
""" 1-number_of_lines.py

    number_of_line func
"""


def number_of_lines(filename=""):
    """number_of_lines func

    returns the number of lines of a text file

    Args:
        filename (str, optional): file. Defaults to "".

    Returns:
        int: number of lines
    """
    count = 0

    with open(file=filename, mode="r") as f:
        for line in f:
            count += 1

    return count
