import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]
students = []

try:
    with open(before, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            surname, name = row["name"].split(", ")
            students.append({"first": name, "last": surname, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {before}")

else:
    with open(after, "w", newline="") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
