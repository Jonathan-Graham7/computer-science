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
        if not round(abs(pin)) + 0.00001 > pin:
            return False
        if round(pin) in verify_pin:
            return False
        if -1 * round(pin) in verify_pin:
            return False
        verify_pin.append(round(pin))
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
    except ValueError:
        return False
    return True

def simpleSolveInput(equation):
    if len(equation) != 1:
        while True:
            if '!' in equation:
                factorial_place = equation.index('!')
                if not verifyEquationFormat(equation[factorial_place - 1]):
                    return equation[factorial_place - 1], 'Typo in equation'
                factorial_number = float(equation[factorial_place - 1])
                if round(factorial_number) < factorial_number + 0.00001 and -1 * round(factorial_number) > -1 * factorial_number + 0.00001:
                    equation[factorial_place] = math.factorial(round(equation[factorial_place - 1]))
                else:
                    return factorial_number, 'Tried to compute factorial on non-integer.'
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
    if len(equation) != 1:
        return len(equation), f'Equation was not fully solved, still contained {equation}'
    if not round(abs(equation[0])) + 0.00001 > equation[0]: #checks for accuracy up to 5 decimal places
        return float(equation[0]), f'Equation did not equal an integer'
    return round(equation[0]), 'Valid'

def complexSolveInput(equation):
    equation_list = list(equation)
    equation_list = [term for term in equation_list if term != ' ']
    root_counter = 0
    for term in equation_list:
        if term == 's':
            root_counter += 1
    if root_counter > 7:
        return root_counter, f"Tried to cheat by using square root function too many times"
    if '(' not in equation_list or ')' not in equation_list:
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

def playBall(pin_set, same_frame):
    die = np.random.randint(1, 7, 3).tolist()
    #die = [3, 2, 1]
    while True:
        for pin in pin_set:
            print(pin, end=' ')
        print()
        input_string = f"Enter an equation using {die[0]}, {die[1]}, and {die[2]} or type 'end' to complete the first half of the frame: "
        equation_input = input(input_string)
        if equation_input == 'end':
            break
        is_valid = verifyInput(equation_input, die)
        if is_valid != 'Valid':
            print(colorPrinter(is_valid), 'red')
            continue
        solution = complexSolveInput(equation_input)
        if solution[1] != 'Valid':
            print(colorPrinter(solution[1] + ', ' + str(solution[0]), 'red'))
            continue
        if solution[0] in pin_set:
            print(colorPrinter(equation_input + ' = ' + str(solution[0]), 'green'))
            pin_set[pin_set.index(solution[0])] = colorPrinter('\u2713', 'green')
        else:
            print(colorPrinter(str(solution[0]) + ' is not a pin to hit', 'red'))
    ball_score = scoreKeeper(pin_set)
    if ball_score == len(pin_set):
        if same_frame:
            return "SPARE!"
        return "STRIKE!"
    return str(ball_score)

def main():
    args_given = argParser()
    pins = initializePins(args_given['difficulty'])
    second_ball_check = input("Is this the second ball using the remaining pins? ")
    second_ball = False
    # check if this is the second ball of the frame, and replace the initialized pins with pins to be input
    if re.search(r"^[Yy]", second_ball_check):
        second_ball = True
        while True:
            input_pins = input("Please list the remaining pins in the format 'integer, integer, ...': ").split(',')
            input_pins = [pin.strip() for pin in input_pins]
            input_pins.sort()
            pin_validation = inputPinsValidation(input_pins)
            if pin_validation:
                pins = input_pins
                break
            else:
                print("Please use the format: 'integer, integer, ...'")
                continue
    report_score = playBall(pins, second_ball)
    print(colorPrinter(report_score, 'green'))

if __name__ == "__main__":
    main()