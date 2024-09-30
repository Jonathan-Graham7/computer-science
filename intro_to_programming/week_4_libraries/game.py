"""
I'm thinking of a number between 1 and 100…

What is it?
It's 50! But what if it were more random?

In a file called game.py, implement a program that:

Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random

def main():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
        except ValueError:
            pass
        else:
            if level <= 0:
                pass
            else:
                guessNum(level)
                break

def guessNum(lvl):
    number = random.randint(1, lvl)
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
        except ValueError:
            pass
        else:
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break


if __name__ == "__main__":
    main()