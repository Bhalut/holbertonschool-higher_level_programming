#!/user/bin/python3
"""4-print_square

   print_square function
"""


def print_square(size):
    """print square funtion

    prints a square with the character #

    Args:
        size: length of the square

    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size, end="")
        print()
