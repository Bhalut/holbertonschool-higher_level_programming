#!/usr/bin/python3
""" 2-square.py

    Square class with validation attribute

    Raises:
        TypeError: Error by not be type integer
        ValueError: Error by be negative number
"""


class Square():
    """Square Class

    Class Square with validation attribute
    """

    def __init__(self, size=0):
        """__init__ Constructor

        Contructor with size attribute

        Args:
            size (int, optional): size of Square. Defaults to 0.

        Raises:
            TypeError: Error by not be type integer
            ValueError: Error by be negative number
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
