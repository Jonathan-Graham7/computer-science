import sys
import argparse
import numpy as np
import math
import re

def argParser():
    parser = argparse.ArgumentParser(
        description='A game to create equations that solve for a given set of bowling pins.'
        'Acceptable mathematical operations are +, -, /, *, !, ^, sqrtx, (where x is an integer), xrty (where x and y are integers), '
        'and parenthesis where needed. ex: sqrt4+3-1 = 4 or 3rt(6+2) = 2'
    )
    parser.add_argument(
        '-difficulty',
        help='The amount of numbers that could be negative.',
        type=int,
        choices=range(11),
        metavar='[0-10]',
        default=0
    )
    parser.add_argument(
        '-last',
        help='Indicates if this is the last frame of a game.',
        action=argparse.BooleanOptionalAction,
        default=False
    )
    return vars(parser.parse_args())

def playBall(pin_set, second_ball, score):
    die = np.random.randint(1, 7, 3)
    #die = np.array([2, 2, 1])
    while True:
        for pin in pin_set:
            print(pin, end=' ')
        print()
        input_string = f"Enter an equation using {die[0]}, {die[1]}, and {die[2]} or type 'end' to complete the first half of the frame: "
        if second_ball:
            input_string = f"Enter an equation using {die[0]}, {die[1]}, and {die[2]} or type 'end' to complete the frame: "
        equation_input = input(input_string)
        if equation_input == 'end':
            break
        is_valid = verifyInput(equation_input, die)
        if is_valid != 'Valid':
            print(is_valid)
            continue
        try:
            test = complexSolveInput(equation_input)
        except ValueError:
            print("Typo in equation")
            continue
        if test[1] != 'Valid':
            print(test[1])
            continue
        pin_set = pinUpdate(pin_set, test[0])
    ball_score = scoreKeeper(pin_set, score)
    if ball_score == 10:
        return "STRIKE!"
    if second_ball and score + ball_score == 10:
        return "SPARE!"
    return ball_score

def main():
    args_given = argParser()
    bowling_pins = initializePins(args_given['difficulty'])
    frame_score = 0
    first_ball = False
    ball_1 = playBall(bowling_pins, first_ball, frame_score)
    try:
        first_half_frame_score = int(ball_1)
        print(f"Scored {first_half_frame_score} points in this part of the frame")
        frame_score += first_half_frame_score
    except ValueError:
        return ball_1
    second_ball = True
    ball_2 = playBall(bowling_pins, second_ball, frame_score)
    try:
        second_half_frame_score = int(ball_2)
        print(f"Scored {second_half_frame_score} points in this part of the frame")
        frame_score += second_half_frame_score
    except ValueError:
        return ball_2
    sys.exit()

def initializePins(num_to_randomize):
    pins = list(range(1, 11))
    pin_index_to_alter = np.random.choice(10, num_to_randomize, replace=False)
    for num in pin_index_to_alter:
        pins[num] *= -1
    return pins

def pinUpdate(current_pins_up, latest_input):
    if latest_input in current_pins_up:
        current_pins_up[current_pins_up.index(latest_input)] = '\033[92m\u2713\033[0m'
    return current_pins_up

def scoreKeeper(current_pins_up, current_score):
    still_up = 0
    for pin in current_pins_up:
        try:
            int(pin)
        except ValueError:
            continue
        else:
            still_up += 1
    score = 10 - still_up - current_score
    return score

def verifyInput(equation, die):
    die_list = die.tolist()
    verify_die = []
    acceptable_characters = ['(', ')', '+', '-', '*', '/', '^', 's', 'q', 'r', 't', '!', ' ']
    for entry in equation:
        if entry in acceptable_characters:
            continue
        if entry.isdigit():
            if int(entry) in die_list:
                verify_die.append(int(entry))
                continue
            else:
                return f"Used a number that was not rolled on the die, {entry}."
        return f"Used a character not approved for equations, {entry}."
    die_list.sort()
    verify_die.sort()
    if die_list != verify_die:
        return "Didn't use all of the rolled die."
    return "Valid"

def simpleSolveInput(equation):
    if len(equation) != 1:
        while True:
            if '!' in equation:
                factorial_place = equation.index('!')
                try:
                    equation[factorial_place] = math.factorial(int(equation[factorial_place - 1]))
                except ValueError:
                    return float(equation[factorial_place - 1]), 'Tried to compute factorial on non-integer.'
                else:
                    del equation[factorial_place - 1]
            else:
                break
        while True:
            if '^' in equation or 't' in equation:
                try:
                    root_place = equation.index('t')
                except ValueError:
                    root_place = sys.maxsize
                try:
                    exponent_place = equation.index('^')
                except ValueError:
                    exponent_place = sys.maxsize
                if root_place < exponent_place:
                    if 's' in equation:
                        equation[root_place] = np.sqrt(float(equation[root_place + 1]))
                        del equation[root_place + 1]
                        equation = equation[:root_place - 3] + equation[root_place:]
                    else:
                        equation[root_place] = float(equation[root_place + 1]) ** (1/float(equation[root_place - 2]))
                        del equation[root_place + 1]
                        equation = equation[:root_place - 2] + equation[root_place:]
                else:
                    equation[exponent_place] = np.power(float(equation[exponent_place - 1]), float(equation[exponent_place + 1]))
                    del equation[exponent_place + 1]
                    del equation[exponent_place - 1]
            else:
                break                  
        while True:
            if '*' in equation or '/' in equation:
                try:
                    multiplication_place = equation.index('*')
                except ValueError:
                    multiplication_place = sys.maxsize
                try:
                    division_place = equation.index('/')
                except ValueError:
                    division_place = sys.maxsize
                if multiplication_place < division_place:
                    equation[multiplication_place] = float(equation[multiplication_place - 1]) * float(equation[multiplication_place + 1])
                    del equation[multiplication_place + 1]
                    del equation[multiplication_place - 1]
                else:
                    equation[division_place] = float(equation[division_place - 1]) / float(equation[division_place + 1])
                    del equation[division_place + 1]
                    del equation[division_place - 1]
            else:
                break
        while True:
            if '+' in equation or '-' in equation:
                try:
                    addition_place = equation.index('+')
                except ValueError:
                    addition_place = sys.maxsize
                try:
                    subtraction_place = equation.index('-')
                except ValueError:
                    subtraction_place = sys.maxsize
                if addition_place < subtraction_place:
                    equation[addition_place] = float(equation[addition_place - 1]) + float(equation[addition_place + 1])
                    del equation[addition_place + 1]
                    del equation[addition_place - 1]
                else:
                    equation[subtraction_place] = float(equation[subtraction_place - 1]) - float(equation[subtraction_place + 1])
                    del equation[subtraction_place + 1]
                    del equation[subtraction_place - 1]
            else:
                break
    if len(equation) != 1:
        return len(equation), f'Equation was not fully solved, still contained {equation}.'
    if float(equation[0]) > 1.00001 * int(equation[0]): #checks for accuracy up to 5 decimal places
        return float(equation[0]), f'Equation did not equal an integer, {equation[0]}.'
    print(equation[0])
    return int(equation[0]), 'Valid'
    
def complexSolveInput(equation):
    equation_list = list(equation)
    equation_list = [term for term in equation_list if term != ' ']
    root_counter = 0
    for term in equation_list:
        if term == 's':
            root_counter += 1
    if root_counter > 7:
        return root_counter, f"Tried to cheat by using square root function {root_counter} times."
    if '(' not in equation_list or ')' not in equation_list:
        return simpleSolveInput(equation_list)
    while True:
        open_parenthesis = []
        close_parenthesis = []
        for i, char in enumerate(equation_list):
            if char == '(':
                open_parenthesis.append(i)
            if char == ')':
                close_parenthesis.append(i)
        if len(open_parenthesis) != len(close_parenthesis):
            return len(open_parenthesis) - len(close_parenthesis), f"Opened {len(open_parenthesis)} parethesis " \
                f"and closed {len(close_parenthesis)} parenthesis."
        minimum_space = sys.maxsize
        closest_op = -1
        closest_cp = -1
        for cp in close_parenthesis:
            for op in open_parenthesis:
                if (cp - op) < minimum_space:
                    minimum_space = cp - op
                    closest_op = op
                    closest_cp = cp
        if closest_cp == -1:
            break
        small_test = equation_list[closest_op+1:closest_cp]
        print(small_test)
        small_solve = simpleSolveInput(small_test)
        equation_list[closest_op] = small_solve[0]
        print(small_solve)
        del equation_list[closest_op+1:closest_cp+1]
        print(equation_list)
        continue
    return simpleSolveInput(equation_list)

if __name__ == "__main__":
    main()