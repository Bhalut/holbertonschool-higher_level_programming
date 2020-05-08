#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    for num in range(len(roman_string)):
        if (
            num > 0 and
            roman[roman_string[num]] > roman[roman_string[num - 1]]
        ):
            number += roman[roman_string[num]] - \
                (2 * roman[roman_string[num - 1]])
        else:
            number += roman[roman_string[num]]

    return number
