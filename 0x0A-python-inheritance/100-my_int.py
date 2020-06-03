#!/usr/bin/python3
""" 100-my_int.py

    MyInt class
"""


class MyInt(int):
    """MyInt class

    MyInt inherence
    """

    def __eq__(self, value):
        """__eq__ method

        equality

        Args:
            value (int): value

        Returns:
            boolean: True or False
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """__ne__ method

        Difference

        Args:
            value (int): value

        Returns:
            boolean: True or False
        """
        return super().__eq__(value)
