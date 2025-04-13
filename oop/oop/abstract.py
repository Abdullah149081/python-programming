from abc import ABC, abstractmethod


class Animal(ABC):  # Abstract class Animal
    def __init__(self, name: str):
        self.name = name

    @abstractmethod  # Abstract method that subclasses must implement
    def make_sound(self) -> str:
        pass


class Mammal(Animal):  # Intermediate class Mammal
    def __init__(self, name: str):
        super().__init__(name)

    # Mammal doesn't need to implement make_sound, it's handled by subclasses


class Cat(Mammal):  # Cat is a subclass of Mammal (and Animal)
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):  # Implementing the abstract method
        return f"{self.name} says Meow!"


class Dog(Mammal):  # Dog is a subclass of Mammal (and Animal)
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):  # Implementing the abstract method
        return f"{self.name} says Woof!"


animals = [Cat("Whiskers"), Dog("Rex")]

for animal in animals:
    print(animal.make_sound())
