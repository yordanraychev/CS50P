import sys
import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ").title()
        if len(name) < 1:
            sys.exit()
        names.append(name)
        output = p.join(names)
    except EOFError:
        print('\n')
        print("Adieu, adieu, to " + output)
        break
    else:
        continue
