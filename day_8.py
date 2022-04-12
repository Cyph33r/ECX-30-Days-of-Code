from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase


def encrypt(data: str, shift_value: int) -> str:
    """
    determines the caesar cipher of data given the shift code
    :param data: the data of type string to be encoded
    :param shift_value: the shift value by which the characters are to be shifted. negative values shift backward
    :return: the caesar cipher of the data enter using the shift return as a string
    """
    assert isinstance(data, str), f"Expected class string for parameter data but {data.__class__} was entered"
    assert isinstance(shift_value,
                      int), f"Expected class string for parameter shift_value but {shift_value.__class__} was entered"
    digest = ''
    for char in data:  # if the character is not a letter do not encrypt
        if not char.isalpha():
            digest += char
            continue
        ordinal = lowercase.find(char)
        ordinal_shifted = ordinal + shift_value
        ordinal_shifted = ordinal_shifted % 26
        if char.islower():
            digest += lowercase[ordinal_shifted]
        else:
            digest += uppercase[ordinal_shifted]
    return digest


def decrypt(_cipher, shift_value):
    """
    reverses the caesar cipher given the shift value used to encode
    :param _cipher: the caesar cipher
    :param shift_value: the shift value used to encode
    :return: the original data that would give back the _cipher when encrypted
    """
    assert isinstance(_cipher, str), f"Expected class string for parameter _cipher but {_cipher.__class__} was entered"
    assert isinstance(shift_value,
                      int), f"Expected class string for parameter shift_value but {shift_value.__class__} was entered"
    data = ''
    for char in _cipher:
        if not char.isalpha():  # if the character is a letter do not decrypt
            data += char
            continue
        ordinal = lowercase.find(char)  # get the zero index of the letter
        ordinal_shifted = ordinal - shift_value
        ordinal_shifted = ordinal_shifted % 26  # wrap, it if it passes the limits
        if char.islower():  # if it is lowercase, append a lowercase shifted value
            data += lowercase[ordinal_shifted]
        else:  # else append the uppercase version
            data += uppercase[ordinal_shifted]
    return data


if __name__ == '__main__':
    print('Welcome to Cyph3r\'s cipher machine')
    response = input('Would you be (d)ecrypting or (e)ncrypting today?: ').lower().strip()
    while response not in ('d', 'e'):
        print('Oops!! You gave an invalid response. Let\'s try that again')
        response = input('Would you be (d)ecrypting or (e)ncrypting today: ').lower().strip()
    if response == 'd':
        secret_word = input('Enter your secret word...i promise not to peek( ͡x ͜ʖ ͡x )\n???').strip()
        while True:
            shift = input('Enter your shift value in digits: ').strip()
            try:
                shift = int(shift)
                print(f'Your cipher is {encrypt(secret_word, shift)}')
                break
            except ValueError:
                print("You entered a non digit. Let's try that again")
    else:
        cipher = input('Enter your cipher: ')
        while True:
            shift = input('Enter your shift value in digits: ').strip()
            try:
                shift = int(shift)
                print(f'Your result is {decrypt(cipher, shift)}')
                break
            except ValueError:
                print("You entered a non digit. Let's try that again")
