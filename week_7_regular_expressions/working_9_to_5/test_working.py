from working import convert
import pytest

def main():
    test_hours()
    test_ampm()
    test_errors()


def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_ampm():
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_errors():
    with pytest.raises(ValueError):
        convert("1:70 AM to 22:90 PM")
    with pytest.raises(ValueError):
        convert("1AM to 1PM")
    with pytest.raises(ValueError):
        convert("1AM - 1PM")


if __name__ == "__main__":
    main()
