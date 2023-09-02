from bank import value

def main():
    test_value()
    test_numbers()
    test_case()


def test_value():
    assert value("Hello") == 0
    assert value("Hello, hello") == 0
    assert value("") == 100


def test_numbers():
    assert value("0") == 100
    assert value("4149714791") == 100


def test_case():
    assert value('HELLO') == 0
    assert value('lower') == 100
    assert value('UPPER') == 100


if __name__ == "__main__":
    main()
