def main():
    fuel = percent()
    percent_fuel = round(fuel * 100)
    if percent_fuel <= 1:
        print("E")
    elif percent_fuel >= 99:
        print("F")
    else:
        print(f"{percent_fuel}%")


def percent():
    try:
        while True:
            user_prompt = input("Fraction: ")
            x, y = user_prompt.split("/")
            x = int(x)
            y = int(y)
            result = x / y
            if result <= 1:
                return result
    except (ValueError, ZeroDivisionError):
        user_prompt = input("Fraction: ")
        pass


main()
