age = 10
str_name = "Masud"
print(age)
print(str_name)

#  type checking
print(type(age), type(str_name))

# typecasting
a = str(age)
print(type(a), type(age))

# template literal
name = f"My name is {str_name} ,My age {age}."
print(name)

# python by default input str
user_Input = input()
user_Age = input()

print("Your name", user_Input, "Your age", user_Age)

# operator
print(106 / 3)
print(106 % 3)
print(106 // 3)  # purno vag fol


# loop
for i in range(1, 10, 2):
    print(i, end=" ")

print("\n", end="")

num = [1, 2, 3, 4, 5]

for idx, element in enumerate(num):
    print(idx, element)


#  function
def sum_of_number(num1, num2, num3=0, *num4):
    sum = num1 + num2 + num3
    for n in num4:
        sum += n
    return sum


print(
    sum_of_number(
        1,
        3,
        4,
        4,
        8,
        10,
    )
)
