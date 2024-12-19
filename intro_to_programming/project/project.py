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
        '-continue',
        help='Use this flag if this is the next ball for the same set of pins.',
        action=argparse.BooleanOptionalAction,
        default=False
    )
    return vars(parser.parse_args())

def initializePins(num_to_randomize):
    pins = list(range(1, 11))
    pin_index_to_alter = np.random.choice(10, num_to_randomize, replace=False)
    for num in pin_index_to_alter:
        pins[num] *= -1
    return pins

def inputPinsValidation(input_pins):
    verify_pin = []
    for pin in input_pins:
        try:
            pin = float(pin)
        except ValueError:
            return False
        else:
            if pin > 6 or pin < -6 or pin == 0:
                return False
        if not pin == int(pin):
            return False
        if int(pin) in verify_pin:
            return False
        if -1 * int(pin) in verify_pin:
            return False
        verify_pin.append(int(pin))
    return True
        
def verifyInput(equation, die):
    verify_die = []
    acceptable_characters = ['(', ')', '+', '-', '*', '/', '^', 's', 'q', 'r', 't', '!', ' ']
    for entry in equation:
        if entry in acceptable_characters:
            continue
        if entry.isdigit():
            if int(entry) in die:
                verify_die.append(int(entry))
                continue
            else:
                return f"Used a number that was not rolled on the die, {entry}."
        return f"Used a character not approved for equations, {entry}."
    die.sort()
    verify_die.sort()
    if die != verify_die:
        return "Didn't use all of the rolled die."
    return "Valid"

def verifyEquationFormat(equation_character):
    try:
        float(equation_character)
    except (ValueError, TypeError):
        return False
    return True

def simpleSolveInput(equation):
    if len(equation) != 1:
        while True:
            if '!' in equation:
                factorial_place = equation.index('!')
                if not verifyEquationFormat(equation[factorial_place - 1]):
                    return equation[factorial_place - 1], 'Typo in equation'
                if factorial_place == 0:
                    return equation[0], 'Typo in equation'
                factorial_number = float(equation[factorial_place - 1])
                if factorial_number > 15:
                    return factorial_number, 'Tried to use factorial on too large of a number'
                if int(abs(factorial_number) + 0.00001) + 0.00001 < factorial_number:
                    return factorial_number, 'Tried to compute factorial on non-integer.'
                equation[factorial_place] = math.factorial(round(factorial_number))
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
                if root_place == 0 or root_place == 1 or exponent_place == 0:
                    return equation[0], 'Typo in equation'
                if root_place == len(equation) - 1 or exponent_place == len(equation) - 1:
                    return equation[-1], 'Typo in equation'
                if exponent_place != sys.maxsize:
                    if not verifyEquationFormat(equation[exponent_place + 1]):
                        return equation[exponent_place + 1], 'Typo in equation'
                    if not verifyEquationFormat(equation[exponent_place - 1]):
                        return equation[exponent_place - 1], 'Typo in equation'
                if root_place != sys.maxsize:
                    if 's' not in equation:
                        if not verifyEquationFormat(equation[root_place + 1]):
                            return equation[root_place + 1], 'Typo in equation'
                        if not verifyEquationFormat(equation[root_place - 2]):
                            return equation[root_place - 2], 'Typo in equation'
                    else:
                        if not verifyEquationFormat(equation[root_place + 1]):
                            return equation[root_place + 1], 'Typo in equation'
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
                if multiplication_place == 0 or division_place == 0:
                    return equation[0], 'Typo in equation'
                if multiplication_place == len(equation) - 1 or division_place == len(equation) - 1:
                    return equation[-1], 'Typo in equation'
                if multiplication_place != sys.maxsize:
                    if not verifyEquationFormat(equation[multiplication_place + 1]):
                        return equation[multiplication_place + 1], 'Typo in equation'
                    if not verifyEquationFormat(equation[multiplication_place - 1]):
                        return equation[multiplication_place - 1], 'Typo in equation'
                if division_place != sys.maxsize:
                    if not verifyEquationFormat(equation[division_place + 1]):
                        return equation[division_place + 1], 'Typo in equation'
                    if not verifyEquationFormat(equation[division_place - 1]):
                        return equation[division_place - 1], 'Typo in equation'
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
                if addition_place == 0 or subtraction_place == 0:
                    return equation[0], 'Typo in equation'
                if addition_place == len(equation) - 1 or subtraction_place == len(equation) - 1:
                    return equation[-1], 'Typo in equation'
                if addition_place != sys.maxsize:
                    if not verifyEquationFormat(equation[addition_place + 1]):
                        return equation[addition_place + 1], 'Typo in equation'
                    if not verifyEquationFormat(equation[addition_place - 1]):
                        return equation[addition_place - 1], 'Typo in equation'
                if subtraction_place != sys.maxsize:
                    if not verifyEquationFormat(equation[subtraction_place + 1]):
                        return equation[subtraction_place + 1], 'Typo in equation'
                    if not verifyEquationFormat(equation[subtraction_place - 1]):
                        return equation[subtraction_place - 1], 'Typo in equation'
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
    else:
        try:
            equation[0] = float(equation[0])
        except ValueError:
            return len(equation), f'Unexpected solo character, {equation}'
    if len(equation) != 1:
        return len(equation), f'Equation was not fully solved, still contained {equation}. Most likely due to a typo in the equation.'
    if int(abs(equation[0]) + 0.00001) + 0.00001 < equation[0]: #checks for accuracy up to 5 decimal places
        return float(equation[0]), f'Equation did not equal an integer'
    return round(equation[0]), 'Valid'

def complexSolveInput(equation):
    equation_list = list(equation)
    equation_list = [term for term in equation_list if term != ' ']
    root_counter = 0
    for term in equation_list:
        if term == 's':
            root_counter += 1
    if root_counter >= 7:
        return root_counter, f"Tried to cheat by using square root function too many times"
    if '(' not in equation_list and ')' not in equation_list:
        return simpleSolveInput(equation_list)
    while True:
        for entry in equation_list:
            try:
                entry.isdigit()
                float(entry)
            except (ValueError, AttributeError, IndexError):
                pass
            else:
                if equation_list.index(entry) + 1 < len(equation_list) and equation_list[equation_list.index(entry) + 1] == '(':
                    equation_list.insert(equation_list.index(entry) + 1, '*')
            if entry == ')':
                try:
                    equation_list[equation_list.index(entry) + 1].isdigit()
                    float(equation_list[equation_list.index(entry) + 1])
                except (ValueError, AttributeError, IndexError):
                    pass
                else:
                    equation_list.insert(equation_list.index(entry) + 1, '*')
        open_parenthesis = []
        close_parenthesis = []
        for i, char in enumerate(equation_list):
            if char == '(':
                open_parenthesis.append(i)
            if char == ')':
                close_parenthesis.append(i)
        if len(open_parenthesis) != len(close_parenthesis):
            return len(open_parenthesis) - len(close_parenthesis), f"Opened {len(open_parenthesis)} parethesis " \
                f"and closed {len(close_parenthesis)} parenthesis"
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
        small_equation = equation_list[closest_op + 1:closest_cp]
        small_solve = simpleSolveInput(small_equation)
        if small_solve[1] == 'Typo in equation':
            return small_solve
        equation_list[closest_op] = small_solve[0]
        del equation_list[closest_op + 1:closest_cp + 1]
        continue
    return simpleSolveInput(equation_list)

def colorPrinter(text, color):
    if color == 'red':
        return f"\033[91m{text}\033[00m"
    elif color == 'green':
        return f"\033[92m{text}\033[00m"
    else:
        return 'Color not registered'
    
def scoreKeeper(current_pins_up):
    still_up = 0
    for pin in current_pins_up:
        try:
            int(pin)
        except ValueError:
            continue
        else:
            still_up += 1
    score = len(current_pins_up) - still_up
    return score

def playBall(pin_set, rolled_die, input_equation):
    if input_equation == 'end':
        return 'end'
    is_valid = verifyInput(input_equation, rolled_die)
    if is_valid != 'Valid':
        return colorPrinter(is_valid, 'red')
    solution = complexSolveInput(input_equation)
    if solution[1] != 'Valid':
        return colorPrinter(solution[1] + ', ' + str(solution[0]), 'red')
    if solution[0] not in pin_set:
        return colorPrinter(str(solution[0]) + ' is not a pin to hit', 'red')
    else:
        # feedback to the user to show that their equation is valid
        print(colorPrinter(input_equation + ' = ' + str(solution[0]), 'green'))
        pin_set[pin_set.index(solution[0])] = colorPrinter('\u2713', 'green')
    return pin_set

def main():
    args_given = argParser()
    pins = initializePins(args_given['difficulty'])
    second_ball_check = args_given['continue']
    second_ball = False
    # check if this is the second ball of the frame, and replace the initialized pins with pins to be input
    if second_ball_check:
        second_ball = True
        while True:
            input_pins = input("Please list the remaining pins in the format 'integer, integer, ...': ").split(',')
            input_pins = [pin.strip() for pin in input_pins]
            input_pins.sort()
            pin_validation = inputPinsValidation(input_pins)
            if pin_validation:
                pins = [int(pin) for pin in input_pins]
                break
            else:
                print("Please use the format: 'integer, integer, ...'")
                continue
    die = np.random.randint(1, 7, 3).tolist()
    while True:
        for pin in pins:
            print(pin, end=' ')
        print()
        input_string = f"Enter an equation using {die[0]}, {die[1]}, and {die[2]} or type 'end' to complete the first half of the frame: "
        equation_input = input(input_string)
        pins_left = playBall(pins, die, equation_input)
        if not isinstance(pins_left, list):
            if pins_left == 'end':
                break
            else:
                print(pins_left)
        else:
            pins = pins_left
    ball_score = scoreKeeper(pins)
    if ball_score == len(pins):
        if second_ball:
            report_score = "SPARE!"
        report_score = "STRIKE!"
    report_score = str(ball_score)
    print(colorPrinter('Score: ' + report_score, 'green'))

if __name__ == "__main__":
    main()