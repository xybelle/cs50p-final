import csv
from tabulate import tabulate

student_list = [
    {"stu_id": "1234", "name": "Harry"},
    {"stu_id": "4567", "name": "Ron"},
    {"stu_id": "7890", "name": "Hermione"},
]

gradebook = [
    {'name': 'Harry', 'Potions': '90', 'Charms': '90'},
    {'name': 'Hermione', 'Potions': '80', 'Charms': '100'},
    {'name': 'Ron', 'Potions': '70', 'Charms': '80'}
]

def main():
    main = [
        ["1", "Add Student"],
        ["2", "See Student List"],
        ["3", "Add Grade"],
        ["4", "See student gradebook"],
        ["5", "See all gradebook"],
        ["6", "Calculate Average"],
        ["7", "Exit"],
    ]

    menu = {
        "1": add_student,
        "2": show_list,
        "3": add_grade,
        "4": show_stu_gradebook,
        "5": show_gradebook,
        "6": calculate_ave,
    }

    while True:
        print("Main Menu")
        print(tabulate(main, headers=["Input", "Description"], tablefmt="fancy_outline"))
        selected = input("Select an option: ")
        if selected in menu:
            menu[selected]()
        elif selected == "7":
            print("Exiting...")
            break
        else:
            print("Invalid Input. Please select a valid option.")



def show_list():
    """Allows teacher to view student list"""
    if not student_list:
        print("\033[3mNo students added yet\033[0m\n")
    else:
        print(tabulate(student_list, headers="keys", tablefmt="fancy_outline"))
        back = input("Press enter to go back to main menu\n")
        if back == "":
            return


def add_student():
    """Allows teacher to add student to student list"""
    while True:
        name = input("Student name: ")
        id = input("Student ID: ")
        ids = [student["stu_id"] for student in student_list]
        if not name or not id:
            print("Please enter name/id")
        if id in ids:
            print("Student ID already in use")
        if name.isalpha() and id.isdigit() and id not in ids:
            student_list.append({"stu_id": id, "name": name})
            print("\033[3mStudent successfully added\033[0m\n")
            break


def add_grade():
    """Allows teacher to add a grade for a specific student and assignment/test."""
    while True:
        names = [_["name"] for _ in student_list]
        name = input("Student Name: ")
        if name not in names:
            print("\033[3mInvalid student name\033[0m")
            continue
        subj = input("Subject: ")
        grade = int(input("Grade: "))
        if grade < 0 or grade > 100:
            print("\033[3mInvalid grade input (0-100)\033[0m")
        student_entry = next((entry for entry in gradebook if entry["name"] == name), None)
        if student_entry:
            student_entry[subj] = grade
            print("\033[3mGrade added successfully\033[0m")
        else:
            gradebook.append({"name": name, subj: grade})
            print("\033[3mGrade added successfully\033[0m")
        break


def show_stu_gradebook():
    """Allows teacher to view a student gradebook"""
    names = [_["name"] for _ in student_list]
    try:
        name = input("Student Name: ")
        if name not in names:
            print("\033[3mInvalid student name\033[0m")
            raise ValueError
    except ValueError:
        pass

    stu_gradebook = filter(lambda s: s["name"] == name, gradebook)
    print(tabulate(stu_gradebook, headers="keys", tablefmt="fancy_outline"))
    back = input("Press enter to go back to main menu\n")
    if back == "":
        return


def show_gradebook():
    """Allows teacher to view a student gradebook"""
    print(tabulate(gradebook, headers="keys", tablefmt="fancy_outline"))
    back = input("Press enter to go back to main menu\n")
    if back == "":
        return


def calculate_ave():
    """Calculates the average grade"""
    grades = []
    for student in gradebook:
        stu_grades = {}
        for subject, grade in student.items():
            if subject == "name":
                continue
            stu_grades[subject] = int(grade)
        average_grade = sum(stu_grades.values()) / len(stu_grades) if stu_grades else 0
        grades.append({"name": student["name"], **stu_grades, "ave": average_grade})
    print(tabulate(grades, headers="keys", tablefmt="fancy_outline"))
    get_report = input("Generate report? (Y/N) ").lower()
    if get_report == "y":
        filepath = input("Save as? ")
        return generate_report(grades, filepath)
    else:
        return


def generate_report(grades, filepath):
    """Generate report of all grades for all student"""
    fieldnames = []
    for grade in grades:
        for key in grade.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with open(f"{filepath}.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in grades:
            writer.writerow(row)
    print(f"\033[3mSuccessfully generated: {filepath}.csv\033[0m\n")


if __name__ == "__main__":
    main()
