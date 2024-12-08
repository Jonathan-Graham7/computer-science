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
    pass