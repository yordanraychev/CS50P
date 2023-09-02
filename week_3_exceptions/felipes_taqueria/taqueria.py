total_sum = 0

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while True:
    try:
        user_prompt = input("Item: ").strip().title()
        for item in menu:
            if item == user_prompt:
                total_sum += (menu[item])
                print(f"${total_sum:.2f}")
    except (EOFError, KeyError):
        break
