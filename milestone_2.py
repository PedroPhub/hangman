import random

words_list = ['apple',
              'orange',
              'banana',
              'berry',
              'grape']

def check_input(arg):
    if len(arg) == 1 & arg.isalpha():
        print('Good guess!')
        return 1
    else:
        print("Oops! That is not a valid input.")
        return 0


word = random.choice(words_list)
guess = input('Please enter a letter: ')

check_input(guess)
