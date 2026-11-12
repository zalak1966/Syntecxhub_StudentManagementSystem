from student import Student
from manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n" + "=" * 40)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            grade = input("Enter Student Grade: ").strip()

            if not student_id or not name or not grade:
                print("Error: All fields are required!")
                continue

            student = Student(student_id, name, grade)
            manager.add_student(student)

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            student_id = input("Enter Student ID to update: ").strip()
            name = input("Enter New Name: ").strip()
            grade = input("Enter New Grade: ").strip()

            if not student_id or not name or not grade:
                print("Error: All fields are required!")
                continue

            manager.update_student(student_id, name, grade)

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ").strip()
            manager.delete_student(student_id)

        elif choice == "5":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()