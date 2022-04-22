def arabic_to_roman(arabic: int) -> str:
    """
    Crude implementation of an arabic to roman numeral converter
    :param arabic: The arabic numeral to be converted as a positive integer
    :return: The roman representation of arabic
    """
    assert isinstance(arabic, int), f'Expected one parameter of class int, you pass in a {arabic.__class__}'
    assert arabic > 0, f'Expected a positive integer you entered {arabic}'  # sanitize the input
    roman_mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    to_roman = ''
    arabic_copy = arabic
    for roman_numeral in sorted(roman_mapping.keys(), reverse=True):
        to_remove = arabic_copy // roman_numeral  # check if the current roman numeral can be subtracted from arabic
        while to_remove > 0:  # continue deduction while roman_numeral can be deducted
            arabic_copy -= roman_numeral
            to_roman += roman_mapping[roman_numeral]
            to_remove = arabic_copy // roman_numeral
    return to_roman


if __name__ == '__main__':
    arabic_input = input('To convert to roman numerals, enter your arabic numeral: ')
    while not arabic_input.isnumeric():  # ensure that the input is a string
        arabic_input = input("Please enter a valid arabic numeral: ")
    print(arabic_to_roman(int(arabic_input)))
