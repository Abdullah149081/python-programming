from food_item import FoodItem


class Menu:
    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_menu_item(self, item: FoodItem) -> None:
        self.items.append(item)
        print(f"Item '{item.name}' added to menu.")

    def find_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name: str) -> None:
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"Item '{item_name}' deleted from menu.")
        else:
            print("Item not found")

    def show_menu(self) -> None:
        print("***** Menu *****")
        if not self.items:
            print("Menu is empty.")
            return
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
