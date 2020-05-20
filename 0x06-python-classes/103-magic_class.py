#!/usr/bin/python3
""" 103-magic_class

    class MagicClass

    Raises:
        TypeError: radius must be a number

    Returns:
        number: area
"""

import math


class MagicClass():
    """MagicClass class

    class MagicClass
    """

    def __init__(self, radius=0):
        """__init__ Constructor

        Contructor MagicClass

        Args:
            radius (number): radius

        Raises:
            TypeError: radius must be a number
        """
        self._MagicClass__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self._MagicClass__radius = radius

    def area(self):
        """area Method

        return area

        Returns:
            number: area
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """circumference Method

        return circumference

        Returns:
            number: circumference
        """
        return 2 * math.pi * (self._MagicClass__radius)
