
import json
from student import Student


class StudentManager:

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    # Load student records from JSON file
    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

                for item in data:
                    student = Student(
                        item["student_id"],
                        item["name"],
                        item["grade"]
                    )
                    self.students.append(student)

        except FileNotFoundError:
            self.students = []

    # Save student records to JSON file
    def save_students(self):
        data = [student.to_dict() for student in self.students]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add a new student
    def add_student(self, student):
        for existing in self.students:
            if existing.student_id == student.student_id:
                print("Error: Student ID already exists!")
                return False

        self.students.append(student)
        self.save_students()
        print("Student added successfully!")
        return True

    # Display all students
    def display_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        print("\n" + "=" * 55)
        print(f"{'STUDENT ID':<15} {'NAME':<20} {'GRADE':<10}")
        print("=" * 55)

        for student in self.students:
            student.display_details()

        print("=" * 55)

    # Update student details
    def update_student(self, student_id, new_name, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.name = new_name
                student.grade = new_grade
                self.save_students()
                print("Student updated successfully!")
                return True

        print("Error: Student not found!")
        return False

    # Delete a student
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully!")
                return True

        print("Error: Student not found!")
        return False
