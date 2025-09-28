MIN_LENGTH = 8

password = input(f"Enter a password (minimum length {MIN_LENGTH}): ")

while len(password) < MIN_LENGTH:
    print("Password must be at least 8 characters long")
    password = input("Enter a password: ")

print("*" * len(password))

