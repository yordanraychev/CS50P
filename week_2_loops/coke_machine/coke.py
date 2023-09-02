amount_due = 50

while True:
    print(f"Amount Due: {amount_due}")
    user_input = int(input("Insert coin: "))
    if user_input == 5 or user_input == 10 or user_input == 25:
        amount_due -= user_input
        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
            break
    else:
        continue
