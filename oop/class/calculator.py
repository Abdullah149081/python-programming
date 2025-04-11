class Calculator:
    brand = "Casio MS990"

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def mul(num1, num2):
        return num1 * num2

    @staticmethod
    def div(num1, num2):
        return num1 % num2


print(Calculator.add(2, 2))
print(Calculator.mul(5, 2))
print(Calculator.div(5, 5))
