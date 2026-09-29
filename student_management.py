import json
import os

DATA_FILE = "students.json"


def load_students():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def generate_student_id(students):
    if not students:
        return 1
    return max(student["id"] for student in students) + 1


def add_student(students):
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Please enter a valid age.")
        return

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    student = {
        "id": generate_student_id(students),
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print(f"Student added successfully! Student ID: {student['id']}")


def view_students(students):
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    print("-" * 65)
    print(f"{'ID':<5}{'Name':<25}{'Age':<10}{'Course':<25}")
    print("-" * 65)

    for student in students:
        print(
            f"{student['id']:<5}"
            f"{student['name'][:23]:<25}"
            f"{student['age']:<10}"
            f"{student['course'][:23]:<25}"
        )

    print("-" * 65)


def search_student(students):
    print("\n--- Search Student ---")

    keyword = input("Enter student name or course: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = [
        student for student in students
        if keyword in student["name"].lower()
        or keyword in student["course"].lower()
    ]

    if not results:
        print("No matching students found.")
        return

    for student in results:
        print("-" * 40)
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")


def update_student(students):
    print("\n--- Update Student ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    student = next(
        (student for student in students if student["id"] == student_id),
        None
    )

    if student is None:
        print("Student not found.")
        return

    name = input(f"Enter new name [{student['name']}]: ").strip()
    course = input(f"Enter new course [{student['course']}]: ").strip()
    age_input = input(f"Enter new age [{student['age']}]: ").strip()

    if name:
        student["name"] = name

    if course:
        student["course"] = course

    if age_input:
        try:
            student["age"] = int(age_input)
        except ValueError:
            print("Invalid age. Previous age retained.")

    save_students(students)
    print("Student details updated successfully.")


def delete_student(students):
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    student = next(
        (student for student in students if student["id"] == student_id),
        None
    )

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)

    print(f"Student '{student['name']}' deleted successfully.")


def show_menu():
    print("\n" + "=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)


def main():
    students = load_students()

    print("\nWelcome to Student Management System!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("\nThank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
