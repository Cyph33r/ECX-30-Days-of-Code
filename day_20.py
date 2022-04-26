from re import compile
from time import sleep


def countdown():
    """
    Simple countdown timer
    """
    seconds = 0
    verify_pattern = compile(r'(\d+[Dd])?\s*(\d+[hH])?\s*(\d+[mM])?\s*(\d+[Ss])?')  # regex pattern to verify input
    split_pattern = compile(r'\d+[DdHhMmSs]')  # regex pattern to get each unit
    time = input("Enter timer e.g 10d 9h 8m 50s: ").strip()
    while not verify_pattern.fullmatch(time):  # validate input
        print("You entered an invalid timer.Let's try that again")
        time = input("Enter timer e.g 10d 9h 8m 50s: ").strip()
    units = split_pattern.findall(time)  # get the units
    for unit in units:
        ending = unit[-1].lower()  # get the time unit e.g d or m since it is the last character
        digit = int(unit[:-1])  # get the time digit
        endings = {'d': 86_400, 'h': 3_600, 'm': 60, 's': 1}  # conversion to second for each unit
        seconds += endings[ending] * digit  # convert each unit to second and  add to the countdown
    while seconds:  # countdown
        print(f'{seconds} seconds left')
        seconds -= 1
        sleep(1)
    print('Time up!!!')
    while True:
        print('\a')
        sleep(0.6)


if __name__ == '__main__':
    countdown()
