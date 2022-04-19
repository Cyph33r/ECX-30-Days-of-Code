from random import randint

games_played = 0
games_won = 0


def higher_or_lower():
    def get_guess(prompt: str) -> int:
        """
        Utility function to get a numeric guess from the user
        :param prompt: the prompt to be passed into the input method
        :return: the guess the user inputted as an int
        """
        response = input(prompt).strip()  # get the guess
        while not response.isnumeric():  # ensure that it is numeric
            print('You did\'nt enter a valid number. Let\'s try that again.')
            response = input(prompt).strip()
        return int(response)  # return the response as an int

    print('Let\'s play a game. I\'ll pick a number between 1 and 100, and you try to guess it')
    play_again = True
    while play_again:
        guess_count = 0
        computers_number = randint(1, 100)  # generate a random between 1-100
        users_guess = get_guess('What is your first guess: ')  # get player's first guess
        while True:
            guess_count += 1  # increment the number of guesses
            if users_guess == computers_number:  # check if the player got the number
                print(f'You got it in {guess_count} guesses! My number was {computers_number}')
                break  # end the game
            if guess_count == 5:  # check if the player has run out of guesses
                print('You did\'nt get the number in 5 guesses.')
                print(f'You lose. My number was {computers_number}')
                break  # end the game
            if users_guess < computers_number:  # report the proximity of the score to the generated number
                users_guess = get_guess('That\'s too low. Try again: ')
            else:
                users_guess = get_guess('That\'s too high. Try again: ')
        play_again_str = input('Would you like to play again? y/n ').strip().lower()
        if play_again_str == 'n':
            play_again = False
    print(f'\nYou played {games_played} games')
    print(f'and you won {games_won} of those game')
    print('Thanks for playing. Goodbye.')


if __name__ == '__main__':
    higher_or_lower()
