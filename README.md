# student gradebook
#### Video Demo: https://youtu.be/qNe4QKkWzBs
#### Description:

My final project for CS50p 2024 online course offered by Harvard University. The student gradebook offers users to add students and their grades for each test(s) and to calculate their averages that can also be exported as CSV.

1. **project.py**
    - Contains functions:
        - `main` : Displays the menu options: to add student, see full student list, add grade, see gradebook per student and all, and calculate average.
        - `show_list` : Allow users to view the student list. If there are no students in the list it will also let the user know
        - `add_student` : Allow user to add student to the list. If no name or id was entered it will prompt again until user enter a valid name and id. Names must be alphabetical and ids must be numbers otherwise will print a message and prompt again. Also, it ensures that the student id is unique otherwise will print a message and prompt again.
        - `add_grade` : Allow users to add grade per student and assignment/test. Requires that the name entered is already in the list. It also checks that the grade is 0 - 100. Then updates gradebook list.
        - `show_stu_gradebook` : Allow users to view a particular student's gradebook. Requires to enter a valid student name (already in list). It then prints the student scores using tabulate for better viewing
        - `show_gradebook` : Allow users to view the entire gradebook (all students) also using tabulate for better viewing.
        - `calculate_ave` : Calculates and displays the average grade of all students. Initialize a grades list with student name(s), subject(s): grade(s), and average(s). User have the option to generate a CSV report, if so they are required to enter a filepath, otherwise go back to main menu.
        - `generate_report` : Takes the grades and filepath from `calculate_ave` to write CSV.
2. **test_project.py**
    - Contains functions:
        - `test_show_list_empty` : For testing `show_list` assuming `student_list` is empty using monkeypatch.
        - `test_show_list_not_empty` : For testing `show_list` assuming `student_list` have entry/entries.
        - `test_add_student_new` : For testing `add_student` for adding a new student (not in the list yet).
        - `test_add_student_none` : For testing `add_student` assuming user didn't enter a valid name/id.
        - `test_add_student_not_new` : For testing `add_student` assuming the id entered is already in use.
        - `test_generate_report` : For testing `generate_report` asserting prints success message and CSV generated contains temp gradebook.
