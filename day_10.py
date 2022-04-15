MAX_ATTEMPTS = 4
USSD_CODE = '*894#'


def bank_service(ussd_code):
    secret_pin = '1234'  # hardcoded passcode
    account_balance = 1_000_000  # account balance
    if ussd_code != USSD_CODE:  # confirm ussd code
        print('Invalid USSD Code. Terminating session...')
        exit(0)

    def get_account():  # helper function to get account number for transferring
        account_number_input = input('Enter recipient account: ').strip()
        while not account_number_input.isnumeric() or len(account_number_input) != 10:
            print('Account number should be 10 digits. Let\'s try that again')
            account_number_input = input('Enter recipient account: ').strip()
        for index, bank in enumerate(banks):
            print(f'{index + 1}. {bank}')
        bank = input('Select recipient bank: ').strip()
        while not bank.isnumeric() or not (0 < int(bank) <= len(banks)):
            print(f'Please select bank from the list above 1 - {len(banks)}. Let\'s try that again.')
            bank = input('Select recipient bank: ').strip()
        return banks[int(bank) - 1], account_number_input

    def get_amount() -> int:  # helper function to get transaction amount
        amount = input('Enter amount: ').strip()
        while not amount.isnumeric() and int(amount) > 0:  # ensure that the customer enters a positive integer
            print('Invalid input. Let\'s try that again')
            amount = input('Enter amount: ').strip()
        return int(amount)

    def withdraw(amount: int) -> bool:  # helper function to withdraw money from customer balance
        nonlocal account_balance  # ensure we are using the account_balance defined in the outer scope
        if amount <= account_balance:
            account_balance -= amount
            return True
        print('Insufficient funds. Terminating session...')
        exit(0)

    def confirm_pin(tries: int = 0) -> bool:  # confirm passcode
        if tries >= MAX_ATTEMPTS:  # if the user has attempted the pin 4 time terminate session
            print('You have failed to enter your pin correctly after 4 attempts. Terminating session...')
            exit(0)
        pin = input(f'Enter your secret PIN(Attempts left : {MAX_ATTEMPTS - tries}): ').strip()
        while not pin.isnumeric() or len(pin) != 4:  # check if the passcode is legal
            print('You entered an invalid response, your pin is a 4-digit number. Let\'s try that again')
            pin = input(f'Enter your secret PIN(Attempts left : {MAX_ATTEMPTS - tries}): ').strip()
        if pin != secret_pin:
            print("You entered an incorrect Pin")
            confirm_pin(tries + 1)  # increase the attempts everytime that the customer enter a legal passcode
            return False
        return True

    banks = ['Access bank', 'First Bank', 'Kuda MFB', 'Zenith Bank', 'Polaris Bank', 'United Bank of Africa',
             'First City Monument Bank', 'Guaranty Trust Bank', 'Cyph3r Bank']
    print('Welcome to Cyph3r\'s banking services')
    print('What services would we be providing you today')
    print('''
1. Send airtime(self)
2. Send airtime(3rd party)
3. Transfer money
4. Check balance 
    ''')
    while True:
        try:
            response = input('Enter your response: ').strip()
            if response not in ('1', '2', '3', '4'):
                raise ValueError
            break
        except ValueError:
            print('You entered an invalid response. Let\'s try that again')
    confirm_pin()  # confirm passcode before performing any transaction
    if response == '1':  # send airtime(self)
        amount_input = get_amount()  # get amount to recharge from user
        if withdraw(amount_input):  # check if the user has sufficient balance
            print('Recharge successful')
    elif response == '2':  # send airtime(3rd party)
        number = input('Enter recipient phone number: ').strip()
        amount_input = get_amount()
        if withdraw(amount_input):
            print(f'Sending {amount_input} to {number}')
    elif response == '3':  # transfer money
        account = get_account()
        amount_input = get_amount()
        if withdraw(amount_input):
            print(f'Sending {amount_input} to {account[0]} ACC NO: {account[1]}')
    elif response == '4':  # check balance
        print(f'Your balance is NGN{account_balance}')


if __name__ == '__main__':
    bank_service('*894#')
