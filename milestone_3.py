

def ask_for_input():
    guess = input('Please enter a letter: ')
    guess_lower = guess.lower()
    if len(guess) == 1 & guess.isalpha():
        check_guess(guess)
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return 0

def check_guess(guess):
    word = 'apple'
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

while True:
    if ask_for_input() != 0:
        break



