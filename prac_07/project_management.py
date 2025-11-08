"""
CP1404 Practical 07 - Project Management
Estimated: 1 Hour
Actual:
"""

import datetime
from project import Project
from operator import attrgetter

DEFAULT_FILENAME = "projects.txt"
DATE_INPUT_FORMATS = ("%d/%m/%Y", "%d/%m/%y")

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
            filename = input("Filename to load: ").strip() or DEFAULT_FILENAME
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"File not found: {filename}")
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
    print("Thank you for using custom-built project management software.")


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
    """Ask for filename and then save projects to it"""
    filename = input("Filename to save projects to: ").strip() or DEFAULT_FILENAME

    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion", file=out_file)
        for p in projects:
            start_str = p.start_date.strftime("%d/%m/%Y")
            print(f"{p.name}\t{start_str}\t{p.priority}\t{p.cost_estimate}\t{p.completion}", file=out_file)
    print(f"Saved {len(projects)} projects to {filename}")


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
    """Ask user for date, then filter projects that start after it"""
    date_string = input("Show projects that start after date (dd/mm/yy): ").strip()
    try:
        after = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        after = datetime.datetime.strptime(date_string, "%d/%m/%y").date()

    filtered = [p for p in projects if p.start_date >= after]
    filtered.sort(key=attrgetter("start_date"))

    for p in filtered:
        print(p)


def add_new_project(projects):
    print("add new project")


def update_project(projects):
    print("update project")


if __name__ == "__main__":
    main()


