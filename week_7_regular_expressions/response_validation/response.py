import validators

def main():
    print(response(input("Text: ")))


def response(n):
    if validators.email(n):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
    