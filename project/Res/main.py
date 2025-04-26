from food_item import FoodItem
from users import Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order

# Create a restaurant instance
mamar_restaurant = Restaurant("Mamar Restaurant")


def customer_menu() -> None:
    print("\n--- Customer Registration ---")
    name: str = input("Enter Your Name: ")
    email: str = input("Enter Your Email: ")
    phone: str = input("Enter Your Phone: ")
    address: str = input("Enter Your Address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"\nWelcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        try:
            choice: int = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name: str = input("Enter item name: ")
            try:
                item_quantity: int = int(input("Enter item quantity: "))
            except ValueError:
                print("Quantity must be a number.")
                continue
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Choice. Try again.")


def admin_menu() -> None:
    print("\n--- Admin Login ---")
    name: str = input("Enter Your Name: ")
    email: str = input("Enter Your Email: ")
    phone: str = input("Enter Your Phone: ")
    address: str = input("Enter Your Address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"\nWelcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Menu Items")
        print("5. Delete Item")
        print("6. Exit")

        try:
            choice: int = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item_name: str = input("Enter Item Name: ")
            try:
                item_price: int = int(input("Enter Item Price: "))
                item_quantity: int = int(input("Enter Item Quantity: "))
            except ValueError:
                print("Price and quantity must be numbers.")
                continue
            item = FoodItem(name=item_name, price=item_price, quantity=item_quantity)
            admin.add_new_item(mamar_restaurant, item)

        elif choice == 2:
            name: str = input("Enter Employee Name: ")
            phone: str = input("Enter Employee Phone: ")
            email: str = input("Enter Employee Email: ")
            designation: str = input("Enter Employee Designation: ")
            try:
                age: int = int(input("Enter Employee Age: "))
                salary: int = int(input("Enter Employee Salary: "))
            except ValueError:
                print("Age and Salary must be numbers.")
                continue
            address: str = input("Enter Employee Address: ")
            employee = Employee(
                name=name,
                email=email,
                phone=phone,
                address=address,
                age=age,
                designation=designation,
                salary=salary,
            )
            admin.add_employee(mamar_restaurant, employee)

        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name: str = input("Enter Item Name to Delete: ")
            admin.remove_item(mamar_restaurant, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Choice. Try again.")


def main() -> None:
    while True:
        print("\n====== Welcome to Mamar Restaurant ======")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

        try:
            choice: int = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            customer_menu()
        elif choice == 2:
            admin_menu()
        elif choice == 3:
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid Choice. Try again.")


if __name__ == "__main__":
    main()
