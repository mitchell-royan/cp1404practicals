"""
CP1404 - Practical 03
Files
"""

# 1. Write users name to a file. Open and close
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2. Opens, reads and prints
file = open("name.txt", "r")
name_from_file = file.read()
file.close()
print(f"Hi {name_from_file}!")

# 3. Open text file, read first 2 numbers, add them together then prints the result
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
print(result)

# 4. Read numbers from file, compute total
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)

