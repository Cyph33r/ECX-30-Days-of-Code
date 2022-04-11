from math import modf
from typing import Union, List


def to_hex(number: Union[int, float]) -> str:
    # check for illegal arguments
    assert (isinstance(number, int) or isinstance(number, float))
    assert number > 0

    # possible hexadecimal numbers with their base 10 conversion as their indices
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    number = float(number)  # convert the number to a float so simplify conversion of decimal part
    converted_whole: List = []
    converted_decimal: List = []
    decimal, whole = modf(number)  # get the decimal and whole counterparts of the number
    whole = int(whole)  # convert the whole part to an integer for easy manipulation

    while True:
        quotient = whole // 16  # whole part of division
        remainder = whole % 16  # remainder part of division
        converted_whole.insert(0,
                               remainder)  # insert to the start of the list so the first item would be the last added
        whole = quotient
        if whole < 16:
            converted_whole.insert(0, whole)  # when the whole part can no longer produce quotients add the remainder
            break

    while True:
        product = decimal * 16
        remainder, _hex = modf(product)  # get the decimal and whole part of the division
        converted_decimal.append(int(_hex))  # append the whole part
        decimal = remainder
        if remainder == 0 or remainder < 1e-100:  # stop when the remainder
            break

    converted_whole = list(map(lambda x: hex_digits[x], converted_whole))
    converted_decimal = list(map(lambda x: hex_digits[x], converted_decimal))
    return ''.join(converted_whole) + '.' + ''.join(converted_decimal) + '(base 16)'


if __name__ == '__main__':
    print(to_hex(-723))
