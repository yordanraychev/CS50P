from um import count

def main():
    test_whitespace()
    test_word()
    test_casesensitive()


def test_whitespace():
    assert count("um") == 1
    assert count("?um?") == 1
    assert count(" um ") == 1


def test_word():
    assert count("yummy") == 0


def test_casesensitive():
    assert count("um, Um, um") == 3
    assert count("UM") == 1


if __name__ == "__main__":
    main()
