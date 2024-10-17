import working
import pytest

def test_format():
    with pytest.raises(ValueError):
        assert working.convert("not time")
    with pytest.raises(ValueError):
        assert working.convert("9AMto5PM")
    with pytest.raises(ValueError):
        assert working.convert("9.30 AM to 5.15 PM")
    with pytest.raises(ValueError):
        assert working.convert("9 A to 5 P")
    with pytest.raises(ValueError):
        assert working.convert("9 am to 5 pm")

def test_entry():
    with pytest.raises(ValueError):
        assert working.convert("9 AM to 5:60 PM")
    with pytest.raises(ValueError):
        assert working.convert("9:-1 to 5 PM")
    with pytest.raises(ValueError):
        assert working.convert("0 AM to 5 PM")
    with pytest.raises(ValueError):
        assert working.convert("9 AM to 13 PM")

def test_conversion():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("1 AM to 11 AM") == "01:00 to 11:00"
    assert working.convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert working.convert("2 PM to 10 PM") == "14:00 to 22:00"
    assert working.convert("6:26 AM to 3:37 PM") == "06:26 to 15:37"
    assert working.convert("6 AM to 3:37 PM") == "06:00 to 15:37"