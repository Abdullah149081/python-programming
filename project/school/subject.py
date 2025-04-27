from typing import List
from person import Teacher, Student
from school import School


class Subject:
    def __init__(self, name: str, teacher: Teacher) -> None:
        self.name: str = name
        self.teacher: Teacher = teacher
        self.max_marks: int = 100
        self.pass_marks: int = 33

    def exam(self, students: List[Student]) -> None:
        for student in students:
            mark: int = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
