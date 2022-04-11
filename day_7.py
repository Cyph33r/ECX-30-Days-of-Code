from random import randint
from linecache import getline


def play_wordle():
    secret_word = 'monks'  # getline('words.txt', randint(0, 50)).strip()  # get a random word from the word-file
    print(f'the word is {secret_word}')
    round_num = 1  # rounds played
    guess = input(
        'WORDLE \n \nEnter your first guess: ').lower().strip()  # get and sanitise the string for the first guess
    while round_num <= 5:
        if round_num != 1:
            guess = input(
                f"Enter guess {round_num}: ").lower().strip()  # get and sanitise the string for the subsequent guesses
        while len(
                guess) != 5 or not guess.isalpha():  # ensure the guess contains only alphabets and has 5 characters
            print("Only a word of 5 letters is allowed!!, Let's try that again.")
            guess = input(f'Enter guess {round_num}: ')
        feedback = ['x', 'x', 'x', 'x', 'x']  # feedback to display at the end of every guess
        guess_copy = guess
        secret_word_copy = secret_word
        for index, letter in enumerate(secret_word):
            if guess_copy[index] == letter:
                feedback[index] = '√'
                guess_copy = guess_copy[:index] + '0' + guess_copy[index + 1:]  # replace the letter that have been checked with 0
        if feedback.count('√') == 5:  # check if the player guessed the word successfully
            print(f"Congrats. You guess the word after {round_num} attempt/s")
            break
        for index2, letter2 in enumerate(
                secret_word):  # check if the player got a letter in the secret word. Renamed the variables for
            # debugging purposes
            if letter2 in guess_copy:
                feedback[index2] = '+'
                guess_copy = guess_copy.replace(letter2, '0', 1)  # replace the letter that have been checked with 0
        print(f"your feedback is {''.join(feedback)}")
        print(f"ROUND {round_num}")
        round_num += 1
    print(f'GAME OVER\nThe word was {secret_word}')


if __name__ == '__main__':
    play_again = True
    while play_again:
        try:
            play_wordle()
        except KeyboardInterrupt:
            print("\nYou have exited the game")
        if input("Enter x to play again: ").lower().strip() != 'x':
            play_again = False
