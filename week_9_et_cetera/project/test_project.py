from project import end, percentage, bordered
from project import study_english, study_greek
from unittest.mock import patch
from io import StringIO


def main():
    test_bordered()
    test_percentage()
    test_end()
    test_study_english()
    test_study_greek()


def test_bordered():
    text = "Hello World"
    expected_output = "~~~~~~~~~~~\nHello World\n~~~~~~~~~~~"
    assert bordered(text) == expected_output


def test_percentage():
    assert percentage(10, 90) == 10
    assert percentage(1, 1) == 50
    assert percentage(0, 100) == 0


def test_end():
    try:
        end()
    except SystemExit:
        pass
    except Exception as e:
        assert False, f"Function raised an exception: {e}"
    try:
        end()
        assert False, "Function did not exit"
    except SystemExit as e:
        assert e.code == 0, f"Unexpected exit code: {e.code}"


def test_study_english():
    def test_study_english_correct_input():
        user_input = ['greek.csv', '2', 'apple', 'apple', 'banana', 'banana']
        expected_output = "What file do you want to study from? Choose wisely.\nHow many rounds of awesome language learning\
            can you handle? Enter a number:\nLet the language adventure begin!\n1\napple\nCan you translate this\
            tricky word?\nCorrect!\n2\nbanana\nCan you translate this tricky word?\nCorrect!\nDrum roll please…\
            Here are your test results:\nCorrect: 2\nWrong: 0\nYour score: 100.00 %\n\nYou rock! You're crushing\
            this language. Do you want to study more? Type yes/no:\n"
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                study_english()
                assert fake_out.getvalue() == expected_output

    def test_study_english_incorrect_input():
        user_input = ['greek.csv', '2', 'orange', 'apple', 'banana', 'banana']
        expected_output = "What file do you want to study from? Choose wisely.\nHow many rounds of awesome language learning\
            can you handle? Enter a number:\nLet the language adventure begin!\n1\napple\nCan you translate this\
            tricky word?\nOops, that's a no-no. Give it another shot.\nCorrect!\n2\nbanana\nCan you translate this\
            tricky word?\nCorrect!\nDrum roll please… Here are your test results:\nCorrect: 2\nWrong: 0\nYour score:\
            100.00 %\n\nYou rock! You're crushing this language. Do you want to study more? Type yes/no:\n"
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                study_english()
                assert fake_out.getvalue() == expected_output

    def test_study_english_wrong_file():
        user_input = ['greek.csv', '2']
        expected_output = "What file do you want to study from? Choose wisely.\nHow many rounds of awesome language learning\
            can you handle? Enter a number:\nLet the language adventure begin!\nUh-oh, something went wrong.\
            Please try again.\n"
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                study_english()
                assert fake_out.getvalue() == expected_output


def test_study_greek():
    user_input = ['greek.csv', '1', 'no']
    expected_output = "What file do you want to study from? Choose wisely.\nNumber of rounds to study?\
        Enter number:\nLet's start! Type 'yes' then ENTER if you nailed it, 'no' if you messed up.\n1\nCan you translate\
        this tricky word?\nOops, that's a no-no. Give it another shot.\nOops, that's a no-no.\
        Let's skip this one.\nDrum roll please… Here are your test results:\nCorrect: 0\nWrong: 1\nYour score:\
        0.00 %\n\nYou did it! Let's review these words one more time:\nYou rock! You're crushing this language.\
        Do you want to study more? Type yes/no:\n"
    try:
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                study_greek()
                assert fake_out.getvalue() == expected_output
    except StopIteration:
        pass
