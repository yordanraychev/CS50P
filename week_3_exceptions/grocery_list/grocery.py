groceries_list = {}

while True:
    try:
        item = input().upper()
        if item in groceries_list:
            groceries_list[item] += 1
        else:
            groceries_list[item] = 1
    except (EOFError, KeyError):
        for item in sorted(groceries_list):
            print(groceries_list[item], item)
        break
        