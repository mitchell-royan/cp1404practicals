def main():
    min_length = 8

    password = input(f"Enter a password (minimum length {min_length}): ")

    password = get_password(min_length, password)
    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))


def get_password(min_length: int, password: str) -> str:
    while len(password) < min_length:
        print("Password must be at least 8 characters long")
        password = input("Enter a password: ")
    return password


main()
