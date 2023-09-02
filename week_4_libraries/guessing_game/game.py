import random
while True:
    try:
        number = int(input("Level: "))
        random_number = random.randint(1, number)
        guess = int(input("Guess: "))
        if guess < random_number:
            print("Too small!")
            continue
        elif guess > random_number:
            print("Too Large!")
            continue
        else:
            print("Just right!")
    except ValueError:
        continue
    break
