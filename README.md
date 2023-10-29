# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The program asks the user to input a letter at the time, in order to find the random mistery word.

## Rules
-The user has 5 lives to guess the mistery word. 

-Lives are reduced by 1 every time the user inputs a character that does not exist in the word picked by the computer.

-The user can see '_' per each letter in the word picked, as well the number of unique letters that builds the word. As you progress, a correct guess will be displayed in the correct position and the number of unique letters will update.

-The game ends when no more lifes are available, or the user completed the word.