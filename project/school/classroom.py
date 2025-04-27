from typing import List
from person import Student
from subject import Subject


class ClassRoom:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.students: List[Student] = []
        self.subjects: List[Subject] = []

    def add_student(self, student: Student) -> None:
        roll_no: str = f"{self.name}-{len(self.students) + 1}"
        student.id = roll_no
        self.students.append(student)

    def add_subject(self, subject: Subject) -> None:
        self.subjects.append(subject)

    def take_semester_final_exam(self) -> None:
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()
