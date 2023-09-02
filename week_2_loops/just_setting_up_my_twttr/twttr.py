user_input = input("Text: ")

for letter in user_input:
    if letter in ["a", "o", "e", "i", "u"]:
        continue
    elif letter in ["A", "O", "E", "I", "U"]:
        continue
    else:
        print(letter, end="")

print()
