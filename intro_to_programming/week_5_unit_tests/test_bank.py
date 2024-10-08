"""
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below,
wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”,
20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively.
You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.

def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py
"""
import bank

def test_good_greeting():
    assert(bank.value("Hello, sir")) == 0
    assert(bank.value("hello customer 4852")) == 0
    assert(bank.value("HELLO STANLEY!!")) == 0

def test_poor_greeting():
    assert(bank.value("Hi Paul")) == 20
    assert(bank.value("howdy, partner")) == 20
    assert(bank.value("Hit me baby 1 more time")) == 20

def test_no_greeting():
    assert(bank.value("Whatsup!")) == 100
    assert(bank.value("Steve, how's it hangin")) == 100
    assert(bank.value("Greetings, humaniod lifeform")) == 100