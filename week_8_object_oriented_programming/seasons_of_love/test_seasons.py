from seasons import minutes

def main():
    test_invalid()
    test_minutes()


def test_invalid():
    assert minutes(2000, 1, 1) == "Twelve million, four hundred twenty-two thousand, eight hundred eighty minutes"
    assert minutes(1999, 9, 9) == "Twelve million, five hundred eighty-seven thousand forty minutes"


def test_minutes():
    assert minutes(28, 3, 1998) == "Invalid date"


if __name__ == "__main__":
    main()
