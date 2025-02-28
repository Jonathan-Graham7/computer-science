    # Math Bowling Game
    #### Video Demo:  https://youtu.be/VO6RQ2SN7oQ
    #### Description:
    -   A game in which the player(s) rolls three six-sided die, then uses the three die rolls in equations that equal 1 through 10 including
        possibilities for any of those numbers to be negative. The equation must use all three die rolls and can use any of the following operations:
        addition, subtraction, multiplication, division, exponentiation, root extraction, and factorials. Factorials and square roots only require
        a single digit since factorials are performed only on a single integer and square roots are a special case of root extraction with an implied 2
        as the index.
    -   Start the game by calling the python from the command line 'python3 progect.py'. It doesn't track score in the between the frames throughout
        the game, or between ball rolls in the same frame, that will have to be tracked manually. If the player would like to increase the difficulty
        (up to 10) use the command line tag '-difficulty int(#)' where int(#) is the desired difficulty. If this is the next ball roll for the same
        set of pins, use the command line tag '-continue'.
    -   Starting with a '-difficult int(#)' tag will generate a pin set with int(#) negative numbers.
    -   Starting with a '-continue' tag will ask for what pins were remaining and say to input them in the following format
        "Please list the remaining pins in the format 'integer, integer, ...': "
    -   Starting with no tags will generate a pin set [1-10] and three random numbers [1-6] with possible repetition and ask for an equation using the
        three random numbers to equal one of the numbers in the pin set. Valid input characters are '(',')','+','-','*','/','^','s','q','r','t','!',
        and any number [1-6].
    -   Any input that contains an invalid character will return the first invalid character used.
    -   The generated pin set and the randomly chosen die will be printed to the console and ask for an equation to be input. The equation that is
        input will be verified to use only valid characters, and as the equation is being solved, it will be verified to be a valid equation.
    -   Any equation that is invalid will be returned as there being a typo in the equation and an indicator of where and what the typo is.
    -   When the equation is solved, it will be printed to the console with an equal sign and the solution, all in green text. The pin set will be
        updated with a green check mark replacing the pin that was solved for.
    -   Any equation that is solved for a number that is not included in the pin set will be returned as not  solving for a valid pin. If an equation
        solves for a pin that has already been solved for, it will be treated the same as if the number was not in the pin set.
    -   To end the game and have the score counted, type 'end' into the equation input or use the keys 'ctrl-d'. The sore will be returned as a number
        in green text. However, if the score was 10 and the '-continue' tag was not used, the score will be returned as "STRIKE" and if the
        '-continue' tag was used, it will be returned as "SPARE".
    -   A timer was originally implemented, but it was clunky on the command line and taking away from the project. It will be reimplemented when the
        project is moved to be a web app.