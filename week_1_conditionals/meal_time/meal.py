def main():
    user_input = input("Time: ")
    time = convert(user_input)
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes_formatted = float(minutes) / 60
    return float(hours) + minutes_formatted


if __name__ == "__main__":
    main()
