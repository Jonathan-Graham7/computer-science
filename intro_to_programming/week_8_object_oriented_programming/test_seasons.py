import seasons
from datetime import date
import pytest

def test_valid():
    with pytest.raises(ValueError):
        assert seasons.isValid("December 1998")
    with pytest.raises(ValueError):
        assert seasons.isValid("December 1876, 24")
    with pytest.raises(ValueError):
        assert seasons.isValid("05/24/1657")
    with pytest.raises(ValueError):
        assert seasons.isValid("1990-4-27")
    with pytest.raises(ValueError):
        assert seasons.isValid("1989-06-34")
    with pytest.raises(ValueError):
        assert seasons.isValid("1989-13-21")

def test_calculations():
    assert seasons.calculateMinutes(date.today()) == 'Zero'