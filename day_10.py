import re
from random import randint
from hashlib import sha256


class BankApp:

    def __init__(self):
        self.account_number = None
        print('Welcome to Cypher Bank')
        print('To open you account, we\'ll need a few details')

        self.last_name = BankApp.get_customer_name('Last')
        self.middle_name = BankApp.get_customer_name('Middle')
        self.first_name = BankApp.get_customer_name('First')
        self.account_balance = 0.0
        self.generate_acc_no()
        print(f'That\'s it!!! We are glad to have you join us. Your account number is {self.account_number}')

    def __str__(self):
        print(f'Good day f{self.first_name}; Account number: {self.account_number}. Your account balance is: NGN {self.account_balance}')

    @staticmethod
    def get_customer_name(name):
        name = input(f'Please, enter your {name} name: ')
        while len(name) == 0:
            print('You entered an invalid name. Let\'s try that again')
            name = input(f'Please, enter your {name} name: ')
        return name

    @staticmethod
    def get_secret_pin():
        pin = input('Please, enter your secret 4-digit pin: ')
        while not pin.isnumeric() or 0 >= len(pin) >= 4:
            print('You enter ')
            pin = input('Please, enter your secret 4-digit pin: ')

    def generate_acc_no(self):
        self.account_number = randint(100000000000, 999999999999)


if __name__ == '__main__':
    my_account = BankApp()
