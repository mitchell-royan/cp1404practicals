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
    try:
        projects = load_projects(DEFAULT_FILENAME)
        print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    except FileNotFoundError:
        projects = []
        print("No default file found; starting with 0 projects.")

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


def load_projects(filename):
    """Load projects"""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for raw_line in in_file:
            line = raw_line.strip()
            if line == "":
                continue
            name, start_str, priority_s, cost_s, completion_s = line.split("\t")
            start_dt = datetime.datetime.strptime(start_str, "%d/%m/%Y").date()

            project = Project(
                name=name,
                start_date=start_dt,
                priority=int(priority_s),
                cost_estimate=float(cost_s),
                completion=int(completion_s),
            )
            projects.append(project)
        return projects


def save_projects(projects):
    print("save projects")


def display_projects(projects):
    """Display two groups, incomplete and complete, sorted by priority"""
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]
    incomplete.sort()
    completed.sort()
    print("Incomplete projects: ")
    for p in incomplete:
        print(f" {p}")

    print("Completed projects: ")
    for p in completed:
        print(f" {p}")


def filter_projects_by_date(projects):
    print("filter projects")


def add_new_project(projects):
    print("add new project")


def update_project(projects):
    print("update project")


main()

