from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase


def encrypt(data: str, shift_value: int) -> str:
    assert isinstance(data, str), f"Expected class string for parameter data but {data.__class__} was entered"
    assert isinstance(shift_value,
                      int), f"Expected class string for parameter shift but {shift_value.__class__} was entered"
    digest = ''
    for char in data:
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
    assert isinstance(_cipher, str), f"Expected class string for parameter data but {_cipher.__class__} was entered"
    assert isinstance(shift_value,
                      int), f"Expected class string for parameter shift but {shift_value.__class__} was entered"
    digest = ''
    for char in _cipher:
        if not char.isalpha():
            digest += char
            continue
        ordinal = lowercase.find(char)
        ordinal_shifted = ordinal - shift_value
        ordinal_shifted = ordinal_shifted % 26
        if char.islower():
            digest += lowercase[ordinal_shifted]
        else:
            digest += uppercase[ordinal_shifted]
    return digest


if __name__ == '__main__':
    print('Welcome to Cyph3r\'s cipher machine')
    response = input('Would you be (d)ecrypting or (e)ncrypting today: ').lower().strip()
    while response not in ('d', 'e'):
        print('Oops!! You gave an invalid response\nLet\'s try that again')
        response = input('Would you be (d)ecrypting or (e)ncrypting today: ').lower().strip()
    if response == 'd':
        secret_word = input('enter your secret word...i promise not to peek( ͡x ͜ʖ ͡x )\n???').strip()
        while True:
            shift = input('enter your shift value in digits: ').strip()
            try:
                shift = int(shift)
                print(f'Your cipher is {encrypt(secret_word, shift)}')
                break
            except ValueError:
                print("You entered a non digit. Let's try that again")
    else:
        cipher = input('enter your cipher: ')
        while True:
            shift = input('enter your shift value in digits: ').strip()
            try:
                shift = int(shift)
                print(f'Your result is {decrypt(cipher, shift)}')
                break
            except ValueError:
                print("You entered a non digit. Let's try that again")
