from fuel import convert, gauge
import pytest

def main():
    test_division_error()
    test_value_error()
    test_convert_gauge()


def test_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")


def test_convert_gauge():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/1") == 100 and gauge(99) == "F"
    assert convert("0/1") == 0 and gauge(1) == "E"


if __name__ == "__main__":
    main()
