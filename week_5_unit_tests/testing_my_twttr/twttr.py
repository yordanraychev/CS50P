def main():
    user_prompt = input("Text: ")
    final_word = shorten(user_prompt)
    print(f"Output: {final_word}")


def shorten(word):
    omitted = ""
    for i in word:
        if not i.lower() in "aeiou":
            omitted += i
    return omitted


if __name__ == "__main__":
    main()
