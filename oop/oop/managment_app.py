from abc import ABC, abstractmethod


class Person(ABC):  # Abstract Base Class
    def __init__(self, name: str, age: int):
        self.name = name  # Public
        self._age = age  # Protected
        self.__id = id(self)  # Private

    def get_id(self):
        return self.__id

    @abstractmethod
    def introduce(self) -> str:
        """Must be implemented by all subclasses."""
        pass


class Student(Person):  # Inherits from Person
    def __init__(self, name: str, age: int, roll: int, department: str):
        super().__init__(name, age)
        self.roll = roll
        self.department = department

    def introduce(self) -> str:  # Polymorphism
        return f"🎓 Student: {self.name}, Dept: {self.department}, Roll: {self.roll}"


class Teacher(Person):  # Inherits from Person
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self) -> str:  # Polymorphism
        return f"👨‍🏫 Teacher: {self.name}, Teaches: {self.subject}"


# ---------- CLI Application ----------
people = []


def add_student():
    name = input("Student Name: ")
    age = int(input("Age: "))
    roll = int(input("Roll Number: "))
    dept = input("Department: ")
    student = Student(name, age, roll, dept)
    people.append(student)
    print("✅ Student added.")


def add_teacher():
    name = input("Teacher Name: ")
    age = int(input("Age: "))
    subject = input("Subject: ")
    teacher = Teacher(name, age, subject)
    people.append(teacher)
    print("✅ Teacher added.")


def show_introductions():
    if people:
        print("\n📣 Introductions (Polymorphism):")
        for person in people:
            print(person.introduce())
    else:
        print("ℹ️ No entries found.")


def show_ids():
    if people:
        print("\n🔐 Encapsulation (Private ID):")
        for person in people:
            print(f"{person.name}'s ID: {person.get_id()}")
    else:
        print("ℹ️ No entries found.")


# CLI Loop
while True:
    print("\n----- OOP CLI Demo -----")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Show Introductions")
    print("4. Show IDs (Encapsulation)")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_teacher()
    elif choice == "3":
        show_introductions()
    elif choice == "4":
        show_ids()
    elif choice == "5":
        print("👋 Exiting... Bye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
