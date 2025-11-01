"""
CP1404 Practical 05 - Emails
Estimate Time: 25 minutes
Actual Time: 35 minutes
"""


def main():
    """Create dictionary to store users names and emails"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = find_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/N) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def find_name_from_email(email):
    """Extract an expected name based off inputted email"""
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    name = " ".join(parts).title()
    return name


main()
