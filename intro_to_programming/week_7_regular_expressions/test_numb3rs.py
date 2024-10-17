from numb3rs import validate

def test_validate_length():
    assert validate("10.2.5.3.4") == False
    assert validate("10.2.4") == False
    assert validate("10.2..4") == False
    assert validate("") == False
    assert validate("10.2.0.6") == True

def test_validate_values():
    assert validate("10.2.4.m") == False
    assert validate("255.3.4.267") == False
    assert validate("10.-1.3.4") == False
    assert validate("10.2.5.?") == False
    assert validate ("64.37.44.0") == True