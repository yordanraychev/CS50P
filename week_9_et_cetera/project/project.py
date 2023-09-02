import random
import csv
from sys import exit
from colorama import init as colorama_init
from colorama import Fore, Style

colorama_init()

vocabulary = {}


def main():
    print(bordered("Do you want to practice English translation or Greek translation? Type 'english' or 'greek':"))
    practice = input()
    if practice == "english":
        study_english()
    elif practice == "greek":
        study_greek()
    else:
        print(bordered("Invalid input. Please restart the program and enter a valid option."))
        end()
    print(bordered("What file do you want to study from? Choose wisely."))
    filename = input()
    print(bordered("How many rounds of awesome language learning can you handle? Enter a number:"))
    number_of_rounds = int(input())


def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['' + '~' * width + '']
    res.append('' + lines[0] + '')
    res.append('' + '~' * width + '')
    return '\n'.join(res)


def percentage(numerator, denominator):
    return 100 * (float(numerator) / float(numerator + denominator))


def end():
    print(bordered("Bye for now, language ninja!"))
    exit(0)


def study_english():
    print(bordered("What file do you want to study from? Choose wisely."))
    filename = input()
    print(bordered("How many rounds of awesome language learning can you handle? Enter a number:"))
    number_of_rounds = int(input())
    print(bordered("Let the language adventure begin!"))
    right = []
    wrong = []
    with open(filename) as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            vocabulary[row["greek"]] = row["english"]
    turns = 0
    while turns < number_of_rounds:
        for key in vocabulary:
            turns += 1
            print(f"{Fore.YELLOW}{turns}{Style.RESET_ALL}")
            vocab = str(random.choice(list(vocabulary.keys())))
            translation = str(vocabulary[vocab])
            print(vocab)
            print("Can you translate this tricky word?")
            guess = input()
            if guess == translation:
                print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                right.append(vocab)
            elif guess != translation:
                print(f"{Fore.RED}Oops, that's a no-no. Give it another shot.{Style.RESET_ALL}")
                guess2 = input()
                if guess2 == translation:
                    print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                    right.append(vocab)
                else:
                    print(f"{Fore.RED}Oops, that's a no-no. Let's skip this one.{Style.RESET_ALL}")
                    wrong.append(vocab)
            else:
                print(bordered("Uh-oh, something went wrong. Please try again."))
                break
            break
    right_count = len(right)
    wrong_count = len(wrong)
    print(bordered("Drum roll please… Here are your test results:"))
    print(f"{Fore.GREEN}Correct{Style.RESET_ALL}: {right_count}")
    print(f"{Fore.RED}Wrong{Style.RESET_ALL}: {wrong_count}")
    print(f"Your score: {percentage(right_count, wrong_count):.2f} %")
    print()
    if not wrong:
        print(bordered("You rock! You're crushing this language. Do you want to study more? Type yes/no:"))
        next = input()
        if next == "yes":
            study_english()
        elif next == "no":
            end()
    else:
        print("You did it! Let's review these words one more time:\n")
        study_again = ','.join(wrong)
        print(study_again)
        print(bordered("You rock! You're crushing this language. Do you want to study more? Type yes/no:"))
        next = input()
        if next == "yes":
            study_english()
        elif next == "no":
            end()


def study_greek():
    print(bordered("What file do you want to study from? Choose wisely."))
    filename = input()
    print(bordered("Number of rounds to study? Enter number:"))
    number_of_rounds = int(input())
    print(bordered("Let's start! Type 'yes' then ENTER if you nailed it, 'no' if you messed up."))
    right = []
    wrong = []
    with open(filename) as readFile:
        reader = csv.DictReader(readFile)
        for row in reader:
            vocabulary[row["greek"]] = row["english"]
    turns = 0
    while turns < number_of_rounds:
        for key in vocabulary:
            turns += 1
            print(f"{Fore.YELLOW}{turns}{Style.RESET_ALL}")
            vocab = str(random.choice(list(vocabulary.keys())))
            translation = str(vocabulary[vocab])
            print(translation)
            print("Can you translate this tricky word?")
            guess = input()
            if guess == "yes":
                print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                right.append(vocab)
            elif guess != "yes":
                print(f"{Fore.RED}Oops, that's a no-no. Give it another shot.{Style.RESET_ALL}")
                guess2 = input()
                if guess2 == "yes":
                    print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                    right.append(vocab)
                else:
                    print(f"{Fore.RED}Oops, that's a no-no. Let's skip this one.{Style.RESET_ALL}")
                    wrong.append(vocab)
            else:
                print(bordered("Uh-oh, something went wrong. Please try again."))
                break
            break
    right_count = len(right)
    wrong_count = len(wrong)
    print(bordered("Drum roll please… Here are your test results:"))
    print(f"{Fore.GREEN}Correct{Style.RESET_ALL}: {right_count}")
    print(f"{Fore.RED}Wrong{Style.RESET_ALL}: {wrong_count}")
    print(f"Your score: {percentage(right_count, wrong_count):.2f} %")
    print()
    if not wrong:
        print(bordered("You rock! You're crushing this language. Do you want to study more? Type yes/no:"))
        next = input()
        if next == "yes":
            study_greek()
        elif next == "no":
            end()
    else:
        print("You did it! Let's review these words one more time:\n")
        study_again = ','.join(wrong)
        print(study_again)
        print(bordered("You rock! You're crushing this language. Do you want to study more? Type yes/no:"))
        next = input()
        if next == "yes":
            study_greek()
        elif next == "no":
            end()


if __name__ == "__main__":
    main()
