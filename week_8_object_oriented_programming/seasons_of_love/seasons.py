from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Your date of birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")
    print(minutes(year, month, day))


def minutes(year, month, day):
    try:
        date_of_birth = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"
    date_today = date.today()
    difference = date_today - date_of_birth
    mins = int(difference.total_seconds() / 60)
    minutes_message = p.number_to_words(mins, andword="") + " minutes"
    return minutes_message.capitalize()


if __name__ == "__main__":
    main()
