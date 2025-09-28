MENU = """\nMenu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print("Welcome to the score program!")
    score = get_valid_score()
    menu_loop(score)
    print("Thank you for using the program. Farewell!")


def determine_score(score) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score() -> int:
    score = int(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Must be 0-100.")
        score = int(input("Enter a score (0-100): "))
    return score


def show_stars(score: int):
    print("*" * score)


def menu_loop(score: int):
    choice = ""
    while choice.upper() != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Exiting menu...")
        else:
            print("Invalid option, try again.")


main()
