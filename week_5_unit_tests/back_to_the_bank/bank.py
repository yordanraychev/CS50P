def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    greeting_lower = greeting.lower()
    if "hello" in greeting_lower:
        return 0
    elif greeting_lower.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
