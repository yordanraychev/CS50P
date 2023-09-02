import re
import sys

def main():
    user_prompt = input("IPv4 Address: ")
    ip_address = validate(user_prompt)
    print(ip_address)


def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        first = int(match.group(1))
        second = int(match.group(2))
        third = int(match.group(3))
        fourth = int(match.group(4))
        if first <= 255 and second <= 255 and third <= 255 and fourth <= 255 :
            return True
        else :
            return False
    else :
        return False


if __name__ == "__main__":
    main()
