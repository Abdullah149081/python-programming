from menu import Menu
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from users import Employee


class Restaurant:
    def __init__(self, name: str):
        self.name: str = name
        self.employees: list[Employee] = []  # Notice: Employee is in quotes!
        self.menu: Menu = Menu()

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def view_employee(self) -> None:
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
