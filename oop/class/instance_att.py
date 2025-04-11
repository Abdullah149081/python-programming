class Shop:
    store = []

    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_store(self, *item):
        self.store.extend(item)

    def add_cart(self, *item):
        self.cart.extend(item)

    def info(self):
        print(f"{self.name} added to store: {self.store}")
        print(f"{self.name} added to cart: {self.cart}")


mausd = Shop("Abdullah Al Masud")
asad = Shop("Asad")

mausd.add_store("bag", "pen")
mausd.add_cart("book")
mausd.info()

print("\n")

asad.add_store("mobile", "paper")
asad.add_cart("glass")
asad.info()
