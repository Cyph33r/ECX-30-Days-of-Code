from random import randint
from linecache import getline


def play_wordle():
    """
    A simple python wordle game
    """
    secret_word = getline('hardcoded_word_list.txt', randint(0, 50)).strip()  # get a random word from the word-file
    round_num = 1  # rounds played
    guess = input(
        'WORDLE \n \nEnter your first guess: ').lower().strip()  # get and sanitise the string for the first guess
    while round_num <= 6:
        if round_num != 1:
            guess = input(
                f"Enter guess {round_num}: ").lower().strip()  # get and sanitise the string for the subsequent guesses
        while len(
                guess) != 5 or not guess.isalpha():  # ensure the guess contains only alphabets and has 5 characters
            print("Only a word of 5 letters is allowed!!, Let's try that again.")
            guess = input(f'Enter guessed {round_num}: ')
        feedback = ['x', 'x', 'x', 'x', 'x']  # feedback to display at the end of every guess
        guess_copy = guess  # make copies of the guess and the secret word
        secret_word_copy = secret_word
        for index, letter in enumerate(guess_copy):  # checks if any letter is in the right position
            if secret_word_copy[index] == letter:
                feedback[index] = '√'
                guess_copy = guess_copy[:index] + '1' + guess_copy[
                                                        index + 1:]  # if it is, replace it with 0 and 1 in both copies
                secret_word_copy = secret_word_copy[:index] + '0' + secret_word_copy[index + 1:]
        if feedback.count('√') == 5:  # check if the player guessed the word successfully
            print(f"Congrats. You guess the word after {round_num} attempt/s")
            break
        for index, letter in enumerate(guess):  # check if the letter is in what is left
            if letter in secret_word_copy:
                feedback[index] = '+'
                guess_copy = guess_copy[:index] + '1' + guess_copy[index + 1:]
                secret_word_copy.replace(letter, '0', 1)
        print(f"your feedback is {''.join(feedback)}")
        round_num += 1  # increment the round
        print(f"ROUND {round_num}")
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
