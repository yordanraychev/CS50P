greeting = input("Greeting: ")
greeting_lower = greeting.lower()

if "hello" in greeting_lower:
    print("$0")
elif greeting_lower[0] == "h":
    print("$20")
else:
    print("$100")
