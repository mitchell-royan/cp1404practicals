"""
CP1404 - Practical 10
"""

import wikipedia


def main():
    prompt = "Enter page title: "
    title = input(prompt)

    while title.strip() != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        print()  # blank line between queries
        title = input(prompt)

    print("Thank you.")


if __name__ == "__main__":
    main()
