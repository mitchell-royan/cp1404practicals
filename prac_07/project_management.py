"""
CP1404 Practical 07 - Project Management
Estimated: 1 Hour
Actual:
"""

import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_INPUT_FORMATS = ("%d/m/%Y", "%d/%m/%y")

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").strip().upper()
        if choice == "L":
            load_projects(projects)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice")


def load_projects(projects):
    print("load projects")


def save_projects(projects):
    print("save projects")


def display_projects(projects):
    print("display projects")


def filter_projects_by_date(projects):
    print("filter projects")


def add_new_project(projects):
    print("add new project")


def update_project(projects):
    print("update project")


main()

