# This program is a random number guessing game
import random

# Handles the user guessing the correct number
def user_guessing(random_number):
    guess = get_input()
    if int(guess) < random_number:
        print('Too low')
    if int(guess) > random_number:
        print('Too high')
    if int(guess) == random_number:
        return int(guess)
    else:
        return 0

# Gets a random number
def get_random_number():
    return random.randrange(1, 20)

# Gets input from user
def get_input():
    return input('Your guess: ')

# Main function
def main():
    print('Can you guess the number 1 to 20?')
    # Get random number
    random_number = get_random_number()
    # Create variable to test for guess
    guess = 0
    # Loop guessing until user gets the correct number
    while (guess != random_number):
        # Get user guess
        guess = user_guessing(random_number)

    print('Good guess, you got it! The number was: ', random_number)
    return 'Good guess, you got it! The number was: ' + str(random_number)

if __name__ == '__main__':
    # Call main function
    main()
