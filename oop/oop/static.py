class School:
    total_students = 0  # ✅ Class attribute (shared by all instances)

    def __init__(self, student_name, grade):
        self.student_name = student_name  # 🧍 Instance attribute
        self.grade = grade
        School.total_students += 1  # Updating class attribute

    def enroll(self, subject, fees):
        print(f"📝 {self.student_name} enrolled in {subject}. Fees: {fees}.")

    @staticmethod
    def add(a, b):
        """🔢 Static method: Utility function, no access to class or instance"""
        print(f"Addition result: {a + b}")

    @classmethod
    def show_total_students(cls):
        """🏫 Class method: Accesses class attribute
        Class method: that changes the class attribute
        """
        print(f"Total Students Enrolled: {cls.total_students}")


# Creating student instances
student1 = School("Masud", "Grade 10")
student2 = School("Rafi", "Grade 9")

# ✅ Instance method call (needs object)
student1.enroll("Math", 500)

# ✅ Class method: Can be called via instance or class
School.show_total_students()
student1.show_total_students()

# ✅ Static method: Doesn't need instance or class attributes
School.add(5, 3)
student2.add(10, 20)  # Also works, but doesn't use instance data
