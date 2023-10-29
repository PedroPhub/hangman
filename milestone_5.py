import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
    
        #Select word from list
        self.word = random.choice(word_list)
        
        #Create list  of '_' to display
        self.word_guessed = []
        for length in range(len(self.word)):
            self.word_guessed.append('_')    
        print(f'\n{self.word_guessed}')

        #Determine number of unique characters
        self.num_letters = len(list(set(self.word)))
        print(f'Number of unique characters: {self.num_letters}')

        #Initialise empty list for attempted letters
        self.list_of_guesses = []
        print(f'Characters used: {self.list_of_guesses}')

    # Function receives and checks if the guess is on the word from the list
    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        lower_guess = guess.lower()
        #if cycle to check if input letter exists in the word to guess
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            #for cycle to replace '_' for the letter if exists in the word
            for letter in range(0,len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess                 
            self.num_letters -= 1
        
        #Lives are reduced by 1 in case the letter does not exist in the word
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    # Function requests and validate one character as input
    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        guess = input('Please enter a letter: ')
        #Verify if the input is not acceptable
        if not(len(guess) == 1 & guess.isalpha()):
            print("Invalid letter. Please, enter a single alphabetical character.")
        #Check if the guess was already used before
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        #Run check_guess to process the valid guess
        else:
            self.check_guess(guess)
            print(f'\n{self.word_guessed}')
            self.list_of_guesses.append(guess)
            print(self.list_of_guesses)

# Manages the duration/flow of the game
def play_game(word_list):
    num_lives = 5
    print("\nLet's play a game!")
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_letters == 0 and game.num_lives > 0:
            print('You won!')
            break

word_list = ['apple',
            'orange',
            'banana',
            'berry',
            'grape',
            'pineapple',
            'plum',
            'strawberry']

play_game(word_list)