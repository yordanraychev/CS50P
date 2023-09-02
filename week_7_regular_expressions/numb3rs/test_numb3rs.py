from numb3rs import validate

def main():
    test_valid_char()
    test_valid_length()


def test_valid_char():
    assert validate("255.255.255.255") == True
    assert validate("197.487.411.468") == False
    assert validate("0.0.0.0") == True
    assert validate("aaa.bbb.ccc.ddd") == False
    assert validate("!@#.$%^.&*.*&^.%$#") == False


def test_valid_length():
    assert validate("2555.255.255.255") == False
    assert validate("25.2555.25.25") == False
    assert validate("255.255.2555.255") == False
    assert validate("255.255.255.2555") == False


if __name__ == "__main__":
    main()
