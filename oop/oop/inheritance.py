class Institute:
    total_members = 0

    def __init__(self, name: str, age: int, address: str):
        self._name = name
        self._age = age
        self._address = address
        Institute.total_members += 1

    def get_sleep_hours(self, number: float):
        print(f"{self._name} sleeps for {number} hours.")

    def get_summary(self) -> str:
        return f"Name: {self._name}, Age: {self._age}, Address: {self._address}"


class Student(Institute):
    total_students = 0

    def __init__(self, name: str, age: int, address: str, roll: str, dep: str):
        super().__init__(name, age, address)  # Initialize parent class
        self._roll = roll
        self._dep = dep
        Student.total_students += 1

    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base}, Roll: {self._roll}, Department: {self._dep}"


class Teacher(Institute):
    total_teachers = 0

    def __init__(self, name: str, age: int, address: str, designation: str):
        super().__init__(name, age, address)  # Initialize parent class
        self._designation = designation
        Teacher.total_teachers += 1

    def take_class(self, hours: int):
        print(f"{self._name}, a {self._designation}, takes a {hours}-hour class.")

    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base}, Designation: {self._designation}"


students: list[Student] = []
teachers: list[Teacher] = []

while True:
    print("\n----- Institute Management CLI -----")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. View All Students")
    print("4. View All Teachers")
    print("5. View Summary Counts")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        address = input("Address: ")
        roll = input("Roll: ")
        dep = input("Department: ")
        student = Student(name, age, address, roll, dep)
        students.append(student)
        print("✅ Student added.")

    elif choice == "2":
        name = input("Name: ")
        age = int(input("Age: "))
        address = input("Address: ")
        designation = input("Designation: ")
        teacher = Teacher(name, age, address, designation)
        teachers.append(teacher)
        print("✅ Teacher added.")

    elif choice == "3":
        print("\n--- Students ---")
        if students:
            for s in students:
                print(s.get_summary())
        else:
            print("No students added yet.")

    elif choice == "4":
        print("\n--- Teachers ---")
        if teachers:
            for t in teachers:
                print(t.get_summary())
        else:
            print("No teachers added yet.")

    elif choice == "5":
        print(f"\nTotal Members: {Institute.total_members}")
        print(f"Total Students: {Student.total_students}")
        print(f"Total Teachers: {Teacher.total_teachers}")

    elif choice == "6":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
