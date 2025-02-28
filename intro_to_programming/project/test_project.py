import project

def test_initializePins():
    assert(len(project.initializePins(0))) == 10
    assert(len(project.initializePins(1))) == 10
    assert(len(project.initializePins(4))) == 10
    assert(len(project.initializePins(10))) == 10
    negative_holder = []
    for entry in project.initializePins(0):
        if entry < 0:
            negative_holder.append(entry)
    assert(len(negative_holder)) == 0
    negative_holder = []
    for entry in project.initializePins(1):
        if entry < 0:
            negative_holder.append(entry)
    assert(len(negative_holder)) == 1
    negative_holder = []
    for entry in project.initializePins(4):
        if entry < 0:
            negative_holder.append(entry)
    assert(len(negative_holder)) == 4
    negative_holder = []
    for entry in project.initializePins(10):
        if entry < 0:
            negative_holder.append(entry)
    assert(len(negative_holder)) == 10

def test_inputPinsValidation():
    assert(project.inputPinsValidation([1,-3,'a',5])) == False
    assert(project.inputPinsValidation([1,-3,'+',5])) == False
    assert(project.inputPinsValidation([1,-3,5,7])) == False
    assert(project.inputPinsValidation([1,-3,0,2])) == False
    assert(project.inputPinsValidation([1,-3,-4,-9])) == False
    assert(project.inputPinsValidation([1,-3,-4,3])) == False
    assert(project.inputPinsValidation([1,5,-4,5])) == False
    assert(project.inputPinsValidation([1,2.4,-4,5])) == False
    assert(project.inputPinsValidation([1,2,-4,5])) == True

def test_verifyInput():
    acceptable_equation_characters = "()+-*/^sqrt! "
    assert(project.verifyInput(acceptable_equation_characters+'1'+'2'+'5', [1,2,3])) == 'Used a number that was not rolled on the die, 5.'
    assert(project.verifyInput(acceptable_equation_characters+'%'+'1'+'2'+'3', [1,2,3])) == 'Used a character not approved for equations, %.'
    assert(project.verifyInput(acceptable_equation_characters+'1'+'2'+'2', [1,2,3])) == "Didn't use all of the rolled die."
    assert(project.verifyInput(acceptable_equation_characters+'1'+'2', [1,2,3])) == "Didn't use all of the rolled die."
    assert(project.verifyInput(acceptable_equation_characters+'1'+'2'+'3', [1,2,3])) == 'Valid'

def test_verifyEquationFormat():
    assert(project.verifyEquationFormat('a')) == False
    assert(project.verifyEquationFormat('/')) == False
    assert(project.verifyEquationFormat('2')) == True
    assert(project.verifyEquationFormat(2)) == True
    assert(project.verifyEquationFormat(2.4)) == True
    assert(project.verifyEquationFormat(2j)) == False

def test_computeAdditionSubtraction():
    assert(project.simpleSolveInput([2,'+','3'])) == (5, 'Valid')
    assert(project.simpleSolveInput([2,'+','-'])) == ('-', 'Typo in equation')
    assert(project.simpleSolveInput([2,'+','3','-','+',5])) == ('+', 'Typo in equation')
    assert(project.simpleSolveInput(['-','2','1'])) == ('-', 'Typo in equation')
    assert(project.simpleSolveInput(['2','1','+'])) == ('+', 'Typo in equation')

def test_computeMultiplicationDivision():
    assert(project.simpleSolveInput([2,'*','3'])) == (6, 'Valid')
    assert(project.simpleSolveInput([2,'*','-'])) == ('-', 'Typo in equation')
    assert(project.simpleSolveInput([2,'+','3','/','+',5])) == ('+', 'Typo in equation')
    assert(project.simpleSolveInput(['*','2','1'])) == ('*', 'Typo in equation')
    assert(project.simpleSolveInput(['2','1','/'])) == ('/', 'Typo in equation')
    assert(project.simpleSolveInput([1,'/','3'])) == (1/3, 'Equation did not equal an integer')
    assert(project.simpleSolveInput([2,'/',3])) == (2/3, 'Equation did not equal an integer')

def test_computeExponentiationRootExtraction():
    assert(project.simpleSolveInput([2,'^','3'])) == (8, 'Valid')
    assert(project.simpleSolveInput([3,'r','t','8'])) == (2, 'Valid')
    assert(project.simpleSolveInput(['s','q','r','t','9'])) == (3, 'Valid')
    assert(project.simpleSolveInput(['s','q','r','t','6','^',2])) == (6, 'Valid')
    assert(project.simpleSolveInput([3,'r','t','8','^','2'])) == (4, 'Valid')
    assert(project.simpleSolveInput(['s','q','r','t','3','^','4'])) == (9, 'Valid')
    assert(project.simpleSolveInput([2,'^','-'])) == ('-', 'Typo in equation')
    assert(project.simpleSolveInput([2,'+','3','r','t','+',5])) == ('+', 'Typo in equation')
    assert(project.simpleSolveInput(['r','t','2','1'])) == ('r', 'Typo in equation')
    assert(project.simpleSolveInput(['2','1','s','q','r','t'])) == ('t', 'Typo in equation')
    assert(project.simpleSolveInput([3,'r','t','6'])) == (pow(6, 1/3), 'Equation did not equal an integer')
    assert(project.simpleSolveInput(['s','q','r','t',3])) == (pow(3, 1/2), 'Equation did not equal an integer')

def test_computeFactorials():
    rounding_threshold = 0.000009
    assert(project.simpleSolveInput([3,'!'])) == (6, 'Valid')
    assert(project.simpleSolveInput(['4','!'])) == (24, 'Valid')
    assert(project.simpleSolveInput([3,'!','!'])) == (720, 'Valid')
    assert(project.simpleSolveInput(['+','!'])) == ('+', 'Typo in equation')
    assert(project.simpleSolveInput(['!',5])) == ('!', 'Typo in equation')
    assert(project.simpleSolveInput([3 + rounding_threshold,'!'])) == (6, 'Valid')
    assert(project.simpleSolveInput([3.1,'!'])) == (3.1, 'Tried to compute factorial on non-integer.')
    assert(project.complexSolveInput(['2','!','!','!','!','!','!'])) == (2, 'Valid')
    assert(project.complexSolveInput(['16','!'])) == (16, 'Tried to use factorial on too large of a number')
    assert(project.complexSolveInput(['15','!'])) == (1307674368000, 'Valid')
    assert(project.complexSolveInput(['4','!','!',])) == (24, 'Tried to use factorial on too large of a number')
    assert(project.complexSolveInput(['3','!','!'])) == (720, 'Valid')

def test_simpleSolveInput():
    rounding_threshold = 0.000009
    assert(project.simpleSolveInput([1])) == (1, 'Valid')
    assert(project.simpleSolveInput(['1'])) == (1, 'Valid')
    assert(project.simpleSolveInput([1 + rounding_threshold])) == (1, 'Valid')
    assert(project.simpleSolveInput([1 - rounding_threshold])) == (1, 'Valid')
    assert(project.simpleSolveInput([-1 * (1 + rounding_threshold)])) == (-1, 'Valid')
    assert(project.simpleSolveInput([1.1])) == (1.1, 'Equation did not equal an integer')
    assert(project.simpleSolveInput(['1.1'])) == (1.1, 'Equation did not equal an integer')
    assert(project.simpleSolveInput([3, 4])) == (2, 'Equation was not fully solved, still contained [3, 4]. Most likely due to a typo in the equation.')
    assert(project.simpleSolveInput(['3', 4])) == (2, "Equation was not fully solved, still contained ['3', 4]. Most likely due to a typo in the equation.")
    assert(project.simpleSolveInput(['3', '4'])) == (2, "Equation was not fully solved, still contained ['3', '4']. Most likely due to a typo in the equation.")
    assert(project.simpleSolveInput(['*'])) == (1, "Unexpected solo character, ['*']")
    assert(project.simpleSolveInput([3,'!','+','s','q','r','t','4','/','2'])) == (7, 'Valid')
    assert(project.simpleSolveInput(['6','!','/',5,'!','-',3])) == (3, 'Valid')
    assert(project.simpleSolveInput([3,'^','s','q','r','t','4','+','1'])) == ('s', 'Typo in equation')
    
def test_complexSolveInput():
    assert(project.complexSolveInput(
        ['s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(',2,')',')',')',')',')',')',')']
        )) == (7, 'Tried to cheat by using square root function too many times')
    assert(project.complexSolveInput(
        ['s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(','s','q','r','t','(',2,')',')',')',')',')',')']
        )) == (pow(2, 1/64), 'Equation did not equal an integer')
    assert(project.complexSolveInput(['3','+','2','+','1'])) == project.simpleSolveInput(['3','+','2','+','1'])
    assert(project.complexSolveInput(['(','3','+','2','*','2'])) == (1, 'Opened 1 parethesis and closed 0 parenthesis')
    assert(project.complexSolveInput(['3','+','2',')','*','2'])) == (-1, 'Opened 0 parethesis and closed 1 parenthesis')
    assert(project.complexSolveInput(['(','3','+','2',')','*','2'])) == (10, 'Valid')
    assert(project.complexSolveInput(['(','3','+','^','2',')','*','2'])) == project.simpleSolveInput(['3','+','^','2'])
    assert(project.complexSolveInput(['(','3','+','2',')','+','*','2'])) == project.simpleSolveInput([5,'+','*','2'])
    assert(project.complexSolveInput(['2','(','3','+','2',')'])) == (10, 'Valid')
    assert(project.complexSolveInput(['(','3','+','2',')','2'])) == (10, 'Valid')
    assert(project.complexSolveInput(['(','3','+','2',')','2'])) == (10, 'Valid')

def test_colorPrinter():
    assert(project.colorPrinter('thing','red')) == '\033[91mthing\033[00m'
    assert(project.colorPrinter(456,'red')) == '\033[91m456\033[00m'
    assert(project.colorPrinter('thing','green')) == '\033[92mthing\033[00m'
    assert(project.colorPrinter(456,'green')) == '\033[92m456\033[00m'
    assert(project.colorPrinter('thing','blue')) == 'Color not registered'

def test_scoreKeeper():
    assert(project.scoreKeeper([1,2,3,4,5,6,7,8,9,10])) == 0
    assert(project.scoreKeeper([1,2,'pin down',4,5,6,'pin down','pin down',9,10])) == 3
    assert(project.scoreKeeper([1,'pin down',3,4,8,9,'pin down'])) == 2
    assert(project.scoreKeeper(['pin down',2,'pin down','pin down',6,'pin down',9,'pin down'])) == 5
    assert(project.scoreKeeper(['pin down','pin down','pin down','pin down','pin down','pin down','pin down','pin down','pin down','pin down'])) == 10

def test_playBall():
    pin_hit = project.colorPrinter('\u2713', 'green')
    assert(project.playBall([1,2,3,4,5,6,7,8,9,10], [1,2,3], '1+2+3')) == [1,2,3,4,5,pin_hit,7,8,9,10]
    assert(project.playBall([1,2,3,4,5,6,7,8,9,10], [1,2,3], '1-2-3')) == project.colorPrinter('-4 is not a pin to hit', 'red')
    assert(project.playBall([1,2,3,4,5,6,7,8,9,10], [1,2,3], 'sqrt(3+2+1)')) == project.colorPrinter('Equation did not equal an integer' + ', ' + str((3+2+1)**(1/2)), 'red')
    assert(project.playBall([1,2,3,4,5,6,7,8,9,10], [1,2,3], '1+2')) == project.colorPrinter("Didn't use all of the rolled die.", 'red')
    assert(project.playBall([1,2,3,4,5,6,7,8,9,10], [1,2,3], 'end')) == project.colorPrinter('Used a character not approved for equations, e.', 'red')