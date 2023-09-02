user_input = input("What is the Answer to the Great Question of Life, the Universe and Everythin? ")

if user_input.strip() == "42" or user_input.lower().strip() == "forty-two" or user_input.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
