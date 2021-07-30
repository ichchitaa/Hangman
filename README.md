# Hangman game
This project is a word-randomized game of hangman, with a fully implemented GUI. I coded for this using Python and Python Tkinter.

How the game works:
A random word is picked by the game out of a pre-set list of words. On the GUI, the number of blanks corresponding to the length of the selected word are 
displayed. A counter called 'Incorrect guesses' is created and this is initially set to and displayed on the GUI as 0. A hangman frame is shown on the GUI 
as well.
The player is permitted 10 guesses in total and 6 errors. After every wrong guess, the 'Incorrect guesses' increases by 1 and a body part is added to the 
hangman. If 6 wrong guesses are made, the hangman is complete and the game is lost. A message is displayed saying 'Game over! The word was <the word>!'.
If the player correctly guesses the word in 10 guesses (with less than 6 errors made), then a congratulatory message is displayed: 'You guessed the word! 
Well done!'

Taking in input:
The game is designed such that both lowercase and uppercase inputs by the user are accepted. If an invalid input (anything that is not a letter) is 
entered, it is accepted by the program and treated like an error.

The GUI:
I implemented the graphical user interface using Python Tkinter. I made it very colorful, adding different colors for the background and all the various 
text. 
