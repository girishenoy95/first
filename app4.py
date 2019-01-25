# Playing around with functions in python


def demo():  # Defining a function
    print("Hello World")


print("top")
demo()  # Calling a function
print("bottom")

# functions with parameters
def say_hi(name, age):
    print("Hello " + name)
    print("The age is " + str(age))

say_hi("mike", 10)  # Passing data values directly
say_hi("giri", 10)  # Passing data values directly


def raised_to(num1, num2):  # Raised to function
    return pow(num1, num2)  # Returning a value

number1 = input("Please enter a number :")  # Taking input from user
number1 = int(number1)   # Converting to int
number2 = input("Please enter another number :")  # Taking another input from user
number2 = int(number2)   # Converting to int

result = raised_to(number1, number2)  # storing the returned value in a variable

print(result)  # Printing the result


def cube(num3):       # Simple cube function
    return num3*num3*num3

print(cube(number2))
