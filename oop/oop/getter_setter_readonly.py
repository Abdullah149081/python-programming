class User:
    def __init__(self, name, age, salary) -> None:
        self._name = name  # Protected attribute
        self._age = age  # Read-only via property
        self.__salary = salary  # Private attribute

    # Read-only property (no setter defined)
    @property
    def age(self):
        """Get the age (read-only)."""
        return self._age

    # Getter for salary
    @property
    def salary(self):
        """Get the current salary."""
        return self.__salary

    # Setter for salary
    @salary.setter
    def salary(self, value):
        """Increase salary by value (does not allow negative values)."""
        if value < 0:
            print("❌ Salary cannot be negative.")
        else:
            self.__salary += value


masud = User("Masud", 25, 15000)

# 🔍 Accessing read-only age property
print("🧑 Age:", masud.age)  # Output: 25

# 💵 Accessing current salary using the getter
print("💵 Current Salary:", masud.salary)  # Output: 15000

# 💸 Increasing salary using the setter
masud.salary = 5000
print("💸 Updated Salary:", masud.salary)  # Output: 20000

# ❌ Trying to set negative salary
masud.salary = -3000  # Output: '❌ Salary cannot be negative.'
print("💵 Final Salary:", masud.salary)  # Output remains: 20000
