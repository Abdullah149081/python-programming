import random
from typing import Dict, Optional
from classroom import ClassRoom
from school import School


class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Teacher(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def evaluate_exam(self) -> int:
        return random.randint(50, 100)


class Student(Person):
    def __init__(self, name: str, classroom: ClassRoom) -> None:
        super().__init__(name)
        self.classroom: ClassRoom = classroom
        self.__id: Optional[str] = None
        self.marks: Dict[str, int] = {}
        self.subject_grade: Dict[str, str] = {}
        self.grade: Optional[str] = None

    # masud.id == id 
    @property
    def id(self) -> Optional[str]:
        return self.__id
    
    # masud.id = 10
    @id.setter
    def id(self, value: str) -> None:
        self.__id = value

    def calculate_final_grade(self) -> str:
        total: float = 0
        for grade in self.subject_grade.values():
            total += School.grade_to_value(grade)

        if total == 0:
            gpa = 0.0
            self.grade = "F"
        else:
            gpa = total / len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)

        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa:.2f}"
