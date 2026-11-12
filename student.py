
class Student:

    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    # Convert student object into dictionary
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }

    # Display student details
    def display_details(self):
        print(f"{self.student_id:<15} {self.name:<20} {self.grade:<10}")
