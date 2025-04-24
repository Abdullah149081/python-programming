"""
          ┌─────────────────┐
          │     Person      │
          │─────────────────│
          │ + name          │
          │ + age           │
          │ + height        │
          │ + weight        │
          │─────────────────│
          │ + eat()         │
          │ + exercise()    │
          └────────┬────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
┌─────────────┐       ┌────────────────┐
│   Student   │       │    Teacher     │
│─────────────│       │────────────────│
│ + institution│      │ + subject      │
│─────────────│       │────────────────│
│ + eat()     │       │ + eat()        │
│ + exercise()│       │ + exercise()   │
│ + __add__() │       │ + __add__()    │
│ + __mul__() │       │ + __mul__()    │
│ + __len__() │       │ + __len__()    │
│ + __gt__()  │       │ + __gt__()     │
└─────────────┘       └────────────────┘
"""

# ✅ Base class - common to all people
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height  # in cm
        self.weight = weight  # in kg

    def eat(self):
        print("🍛 Regular meal: rice, meat, curry.")

    def exercise(self):
        # 🔁 This method is meant to be overridden in subclasses
        raise NotImplementedError("Each person should have their own way to exercise.")


# ✅ Student class inherits from Person (🔗 Inheritance)
class Student(Person):
    def __init__(self, name, age, height, weight, institution) -> None:
        self.institution = institution
        super().__init__(name, age, height, weight)

    # 🔁 Method Overriding - different version of eat
    def eat(self):
        print("🍔 Student meal: fast food and snacks.")

    # 🔁 Overridden exercise method
    def exercise(self):
        print("🏃‍♂️ Jogging at the campus ground.")

    # ➕ Operator Overloading: + adds age
    def __add__(self, other):
        return self.age + other.age

    # ✖️ Operator Overloading: * multiplies weight
    def __mul__(self, other):
        return self.weight * other.weight

    # 📏 len() overload: returns height
    def __len__(self):
        return self.height

    # ➕ Operator Overloading: > compares age
    def __gt__(self, other):
        return self.age > other.age


# ✅ Teacher class also inherits from Person (🔗 Inheritance)
class Teacher(Person):
    def __init__(self, name, age, height, weight, subject) -> None:
        self.subject = subject
        super().__init__(name, age, height, weight)

    # 🔁 Method Overriding - custom eating habit
    def eat(self):
        print("🥗 Healthy meal: vegetables and fruits.")

    # 🔁 Overridden exercise method
    def exercise(self):
        print("🏋️‍♂️ Gym and light yoga.")

    # ➕ Operator Overloading
    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.weight * other.weight

    def __len__(self):
        return self.height

    def __gt__(self, other):
        return self.age > other.age


# 🧪 Demo
student = Student("Masud", 20, 172, 65, "DU")
teacher = Teacher("John", 35, 180, 75, "Mathematics")

# ➕ Overloading: Add ages
print(student + teacher)

# ✖️ Overloading: Multiply weights
print(student * teacher)

# 📏 Overloading: Get height of student
print(len(student))

# ➕ Overloading: Compare ages
print(teacher > student)

# 🔁 Overridden methods
student.eat()
teacher.exercise()
