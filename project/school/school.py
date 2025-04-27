from typing import Dict
from classroom import ClassRoom
from person import Student, Teacher


class School:
    def __init__(self, name: str, address: str) -> None:
        self.name: str = name
        self.address: str = address
        self.teachers: Dict[str, Teacher] = {}  # subject name -> teacher
        self.classrooms: Dict[str, ClassRoom] = {}  # class name -> classroom

    def add_classroom(self, classroom: ClassRoom) -> None:
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject: str, teacher: Teacher) -> None:
        self.teachers[subject] = teacher

    def student_admission(self, student: Student) -> None:
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks: int) -> str:
        if 80 <= marks <= 100:
            return "A+"
        elif 70 <= marks < 80:
            return "A"
        elif 60 <= marks < 70:
            return "A-"
        elif 50 <= marks < 60:
            return "B"
        elif 40 <= marks < 50:
            return "C"
        elif 33 <= marks < 40:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade: str) -> float:
        grade_map = {
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00,
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value: float) -> str:
        if 4.5 <= value <= 5.0:
            return "A+"
        elif 3.5 <= value < 4.5:
            return "A"
        elif 3.0 <= value < 3.5:
            return "A-"
        elif 2.5 <= value < 3.0:
            return "B"
        elif 2.0 <= value < 2.5:
            return "C"
        elif 1.0 <= value < 2.0:
            return "D"
        else:
            return "F"

    def __repr__(self) -> str:
        for key in self.classrooms.keys():
            print(key)
        print("All Students")
        result = ""
        for key, classroom in self.classrooms.items():
            result += f"---{key.upper()} Classroom Students\n"
            for student in classroom.students:
                result += f"{student.name}\n"
        print(result)

        subject = ""
        for key, classroom in self.classrooms.items():
            subject += f"---{key.upper()} Classroom Subjects\n"
            for sub in classroom.subjects:
                subject += f"{sub.name}\n"
        print(subject)

        print("Students Results")
        for key, classroom in self.classrooms.items():
            for student in classroom.students:
                for sub_name, mark in student.marks.items():
                    print(student.name, sub_name, mark, student.subject_grade[sub_name])
                print(student.calculate_final_grade())
        return ""
