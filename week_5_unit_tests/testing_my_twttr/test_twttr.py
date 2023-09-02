from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("123456") == "123456"
    assert shorten(".,.!?!") == ".,.!?!"


if __name__ == "__main__":
    main()
