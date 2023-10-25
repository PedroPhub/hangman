# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The program requires the user to input a letter at the time, in order to find the random mistery word.
The used has 5 lives to guess the  mistery word. Lives are reduced by 1 every time the user inputs a character 
that does not exist in the word picked by the computer.

The character introduced by used is compared to the word picked randomly from a list when the game starts.

The user can see an '_' per letter in the word picked, as well as unique letters yet to find.

As the game progress, the '_' are replaced  for the correct letter.

The game ends when no more lifes are available, or the word is complete.