#!/usr/bin/python3
""" 7-base_geometry.py

    BaseGeometry class

    Raises:
        Exception: area() is not implemented
        TypeError: must be an integer
        ValueError: must be greater than 0
"""


class BaseGeometry():
    """BaseGeometry Class
    """

    def area(self):
        """area [summary]

        [extended_summary]

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator Method

        Args:
            name (string): name
            value (int): value

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
