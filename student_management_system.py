class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self._email = email        # encapsulated (private-like)
        self.age = age
        self.department = department
        self._marks = []           # private attribute for marks

    def add_marks(self, *marks):
        """Method overloading using *args to add multiple marks"""
        self._marks.extend(marks)

    def calculate_result(self):
        if not self._marks:
            return "No marks available"
        avg = sum(self._marks) / len(self._marks)
        return f"Average Marks: {avg:.2f}"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Email: {self._email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    # Method overriding
    def get_student_type(self):
        return f"Undergraduate Student (Semester {self.semester})"


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    # Method overriding
    def get_student_type(self):
        return f"Graduate Student (Research: {self.research_topic})"


# Demonstration of OOP concepts
if __name__ == "__main__":
    # Creating objects
    s1 = Student("Apon", "S001", "apon@example.com", 20, "Computer Science")
    s2 = UndergraduateStudent("Rafi", "U001", "rafi@example.com", 19, "Engineering", 3)
    s3 = GraduateStudent("Mitu", "G001", "mitu@example.com", 25, "Biology", "Genetics")

    # Adding marks (method overloading with *args)
    s1.add_marks(80, 90, 85)
    s2.add_marks(70, 75)
    s3.add_marks(88, 92, 95, 90)

    # Display info
    s1.display_info()
    print(s1.calculate_result())
    print(s1.get_student_type())

    print("\n---\n")

    s2.display_info()
    print(s2.calculate_result())
    print(s2.get_student_type())

    print("\n---\n")

    s3.display_info()
    print(s3.calculate_result())
    print(s3.get_student_type())
