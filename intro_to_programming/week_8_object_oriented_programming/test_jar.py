from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity ==12

def test_str():
    jar = Jar(3)
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7
    jar.deposit(3)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(6)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)