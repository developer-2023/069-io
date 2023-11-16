# docs.python.org/3/library/functions.html#open
# 7:37:27 Harvard CS50’s Introduction to Programming with Python – Full University Course

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
