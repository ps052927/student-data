Total_students = []


def student_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B+"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"


def add_student():

    name = input("Enter student name: ")
    marks = list(
        map(
            float,
            (input("Enter Phy, Che, Math, Eng, Hindi marks of student: ").split()),
        )
    )
    total_mark = 0
    for i in range(0, 5):
        total_mark += marks[i]
    percent = total_mark / 5
    grade = student_grade(percent)

    student = {"name": name, "marks": marks, "percent": percent, "grade": grade}
    Total_students.append(student)
    print("Student added successfully.\n")


def view_students():
    if len(Total_students) == 0:
        print("No student records found.\n")
        return

    print("\nStudent Records")
    print("----------------------")

    for student in Total_students:

        print(
            "Name :",
            student["name"],
            "\tMarks:",
            student["marks"],
            "\tpercent:",
            student["percent"],
            "\tgrade:",
            student["grade"],
        )
        print()


def search_student():

    search_name = input("Enter student name to search: ")

    for student in Total_students:

        if (
            student["name"].lower() == search_name.lower()
            or student["name"].upper() == search_name.upper()
        ):

            print("\nStudent Found")
            print("----------------")
            print("Name :", student["name"])
            print("Marks:", student["marks"])
            print("percent:", student["percent"])
            print("grade:", student["grade"])
            print()
            return
    print("Student not found.\n")


while True:
    print("===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")
    print()
    if choice == "1":
        for i in range(100):
            add_student()
            n = int(input("Enter new student: 1: yes\t\t2: No"))
            if n == 2:
                break
            elif n == 1:
                pass
            else:
                print("Invalid input")

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice.\n")
