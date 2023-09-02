user_input = input("Name of variable: ")
print("Snake case: ", end = "")

for letter in user_input:
    if letter.isupper():
        print("_" + letter.lower(), end = "")
    else:
        print(letter, end = "")
print()
