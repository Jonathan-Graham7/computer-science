"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer,
or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_fuel.py
"""
import fuel
import pytest

def test_convert():
    assert fuel.convert("4/5") == 80
    with pytest.raises(ZeroDivisionError):
        assert fuel.convert("4/0")
    with pytest.raises(ValueError):
        assert fuel.convert("do/do")
    with pytest.raises(ValueError):
        assert fuel.convert("4/3")

def test_gauge():
    assert(fuel.gauge(0)) == "E"
    assert(fuel.gauge(1)) == "E"
    assert(fuel.gauge(2)) == "2%"
    assert(fuel.gauge(57)) == "57%"
    assert(fuel.gauge(98)) == "98%"
    assert(fuel.gauge(99)) == "F"
    assert(fuel.gauge(100)) == "F"