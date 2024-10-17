import um

def test_in_word():
    assert um.count("yummy tummy album") == 0

def test_not_isolated():
    assert um.count("Um, hello, um, world") == 2
    assert um.count("This um, is yummy ice cream") == 1
    assert um.count("um...Um...UM?!") == 3

def test_correct_count():
    assert um.count("Um, this hammer, um, hit my thumbs") == 2
