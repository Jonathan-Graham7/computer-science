"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below,
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not,
but main is only called if the value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py
"""
import plates

def test_symbols():
    assert(plates.is_valid("jek;l")) == False
    assert(plates.is_valid("jeklp")) == True

def test_length():
    assert(plates.is_valid("l")) == False
    assert(plates.is_valid("shledue")) == False
    assert(plates.is_valid("jcneb")) == True

def test_zeros():
    assert(plates.is_valid("jk08")) == False
    assert(plates.is_valid("jk80")) == True

def test_ending():
    assert(plates.is_valid("jd8es")) == False
    assert(plates.is_valid("p4js8")) == False
    assert(plates.is_valid("nxi845")) == True
    assert(plates.is_valid("8475")) == False