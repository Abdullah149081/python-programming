class Person:
    def __init__(self, name: str, contact_no: int):
        self.name = name  # Public
        self.__contact_no = contact_no  # Private

    def get_contact_no(self):
        return self.__contact_no

    def set_contact_no(self, new_contact: int):
        if isinstance(new_contact, int) and new_contact > 0:
            self.__contact_no = new_contact
        else:
            print("❌ Invalid contact number")

    def show_info(self):
        return f"Name: {self.name}\nContact: {self.get_contact_no()}"


class Student(Person):
    def __init__(self, name: str, roll: int, contact_no: int):
        super().__init__(name, contact_no)
        self._roll = roll  # Protected

    def get_roll(self):
        return self._roll

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nRoll: {self._roll}"


class Teacher(Person):
    def __init__(self, name: str, teacher_id: int, contact_no: int, subject: str):
        super().__init__(name, contact_no)
        self._teacher_id = teacher_id  # Protected
        self.subject = subject

    def get_teacher_id(self):
        return self._teacher_id

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nTeacher ID: {self._teacher_id}\nSubject: {self.subject}"


# Creating instances of Student and Teacher
student1 = Student("Masud", 1490, 1234567890)
teacher1 = Teacher("John", 101, 9876543210, "Mathematics")

# Showing their information using one show_info() method
print("Student Info:")
print(student1.show_info())


print("\nTeacher Info:")
print(teacher1.show_info())


# Print all the attributes and methods of the student1 object
print(dir(student1))
# Accessing the private attribute
print(student1._Person__contact_no)
