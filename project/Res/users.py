from abc import ABC
from orders import Order
from restaurant import Restaurant
from food_item import FoodItem


class User(ABC):
    def __init__(self, name: str, phone: str, email: str, address: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name: str, phone: str, email: str, address: str) -> None:
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant: Restaurant) -> None:
        restaurant.menu.show_menu()

    def add_to_cart(
        self, restaurant: Restaurant, item_name: str, quantity: int
    ) -> None:
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item not found")

    def view_cart(self) -> None:
        print("** View Cart **")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self) -> None:
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()


class Employee(User):
    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
        age: int,
        designation: str,
        salary: float,
    ) -> None:
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} ({self.designation}) - {self.email}"


class Admin(User):
    def __init__(self, name: str, phone: str, email: str, address: str) -> None:
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant: Restaurant, employee: Employee) -> None:
        restaurant.add_employee(employee)

    def view_employee(self, restaurant: Restaurant) -> None:
        restaurant.view_employee()

    def add_new_item(self, restaurant: Restaurant, item: FoodItem) -> None:
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant: Restaurant, item_name: str) -> None:
        restaurant.menu.remove_item(item_name)

    def view_menu(self, restaurant: Restaurant) -> None:
        restaurant.menu.show_menu()
