    # Math Bowling Game
    #### Video Demo:  <URL HERE>
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
    -   Starting with no tags will generate a pin set [1-10] and three random numbers [1-6] with possible repetition and ask for an equation using the
        three random numbers to equal one of the numbers in the pin set. Valid input characters are '(',')','+','-','*','/','^','s','q','r','t','!',
        and any number [1-6]. It will verify that all of the numbers generated were used and only those numbers were used and it will verify that
        equation characters are in valid placement.
    -   Starting with a '-difficult int(#)' tag will generate a pin set with int(#) negative numbers.
    -   Starting with a '-continue' tag will ask for what pins were remaining and say to input them in the following format
        "Please list the remaining pins in the format 'integer, integer, ...': "
    The scope of this project is beyond just this assignment. This step is to simulate the game being played for a single frame with an argument 
    option to simulate the last frame, since the last frame in bowling is slightly different than the rest of the frames. The next piece of the 
    process will be to have the program able to simulate the full ten frames of a bowling game. Following this is to have the game ported to a web 
    application using this python code as the backend. The last thing will be to have a coutdown clock running on the web app so that the program 
    will be fully self regulating and not rely on any external factors in order to fully play properly.

    TODO description for functions