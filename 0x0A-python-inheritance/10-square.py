#!/usr/bin/python3
""" 10-square.py

    Square class

    Returns:
        integer: area
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle: inherent
    """

    def __init__(self, size):
        """__init__ constructor

        contructor of Square

        Args:
            size (integer): size square
        """
        super().integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """area method

        Returns:
            integer: Area
        """
        return self.__size * self.__size
