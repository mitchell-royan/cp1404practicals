"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subject(FILENAME)
    display_subject_details(subjects)


def load_subject(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display subject details in correct format."""
    for subject, lecturer, student_count in subjects:
        print(f"{subject} is taught by {lecturer} and has {student_count} students.")


main()
