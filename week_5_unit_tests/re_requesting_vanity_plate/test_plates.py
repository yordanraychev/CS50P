from plates import is_valid

def main():
    test_length()
    test_start()
    test_zeros()
    test_symbols()
    test_numbers()


def test_length():
    assert is_valid("C") == False
    assert is_valid("CC555") == True
    assert is_valid("CSCSCSCS") == False


def test_start():
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("5C") == False
    assert is_valid("55") == False


def test_zeros():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_symbols():
    assert is_valid("?.,.!?!") == False
    assert is_valid(" CS50 ") == False
    assert is_valid("CS.50") == False


def test_numbers():
    assert is_valid("CCC555") == True
    assert is_valid("555CCC") == False
    assert is_valid("CCC55C") == False


if __name__ == "__main__":
    main()
