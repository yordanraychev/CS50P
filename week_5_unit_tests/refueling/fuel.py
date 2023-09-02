def main():
    user_prompt = input("Fraction: ")
    print(gauge(convert(user_prompt)))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            fraction = (x / y) * 100
            if x > y:
                fraction = input("Fraction: ")
            return int(fraction)
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percent_fuel):
    if percent_fuel <= 1:
        return "E"
    elif percent_fuel >= 99:
        return "F"
    else:
        return f"{percent_fuel}%"


if __name__ == "__main__":
    main()
