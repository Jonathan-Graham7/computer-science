# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for num in range(len(secretWord)):
        if secretWord[num] not in lettersGuessed:
            return False
    return True
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_to_return = ''
    for num in range(len(secretWord)):
        if secretWord[num] not in lettersGuessed:
            word_to_return += '_'
        else:
          word_to_return += secretWord[num]
    return word_to_return
    # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_left = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            letters_left += letter
    return letters_left
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print(f"Secret Word contains {len(secretWord)} letters.")
    letters_guessed = []
    incorrect_letter_count = len(secretWord)
    attempts = 8
    win = False
    while attempts > 0:
        if win:
            break
        print(f"You have {attempts} attempts left")
        print(getAvailableLetters(letters_guessed))
        guess = input("Guess a letter: ")
        if not guess.isalpha() or len(guess) > 1:
            print("Please guess appropriately")
            continue
        letters_guessed.append(guess)
        guessed_word = getGuessedWord(secretWord, letters_guessed)
        if guessed_word.count('_') < incorrect_letter_count:
            print(f"Letter {guess} found in the word!")
            incorrect_letter_count = guessed_word.count('_')
        else:
            print(f"Sorry, {guess} was not in the word.")
            attempts -= 1
        print(guessed_word)
        if isWordGuessed(secretWord, letters_guessed):
            win = True
    if win:
        print(f"Congratulations, the word was {secretWord}!")
    else:
        print(f"Sorry, the word was {secretWord}.")
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
