input_without_emoji = input()
input_with_emoji = input_without_emoji.replace(":)", "🙂").replace(":(", "🙁")
print(input_with_emoji)
