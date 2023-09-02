import contextlib
import random

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        with contextlib.suppress(ValueError):
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError


def generate_integer(level):
    score = 0
    for _ in range(1, 11):
        if level == 1:
            X = random.randint(0, 9)
            Y = random.randint(0, 9)
        elif level == 2:
            X = random.randint(10, 99)
            Y = random.randint(10, 99)
        else:
            X = random.randint(100, 999)
            Y = random.randint(100, 999)

        number_of_tries = 1
        while number_of_tries <= 3:
            try:
                user_answer = int(input(f"{X} + {Y} = "))
            except ValueError:
                print("EEE")
                number_of_tries += 1
                continue
            else:
                answer = X + Y
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    if number_of_tries == 3:
                        print(f"{X} + {Y} = {answer}")
                    number_of_tries += 1
    print()
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
