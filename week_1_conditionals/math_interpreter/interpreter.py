user_input = input("Your operation: ")
x_old, y_old, z_old = user_input.split(" ")
x = int(x_old)
y = str(y_old)
z = int(z_old)
result = 0

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")
