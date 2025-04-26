from typing import Dict
from food_item import FoodItem


class Order:
    def __init__(self) -> None:
        # Dictionary to hold items in the cart: {FoodItem: quantity}
        self.items: Dict[FoodItem, int] = {}

    def add_item(self, item: FoodItem) -> None:
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self, item: FoodItem) -> None:
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self) -> float:
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self) -> None:
        self.items.clear()
