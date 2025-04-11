class Pen:
    manufactured = "Bangladesh"

    # constructor
    def __init__(self, owner, band, price):
        self.owner = owner
        self.band = band
        self.price = price

    def print_info(self):
        print(f"{self.owner} write {self.band} pen this pen price {self.price} taka")


my_pen = Pen("Masud", "Matador", 5)

my_pen.print_info()
