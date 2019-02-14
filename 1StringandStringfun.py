from math import *  # importing packages a.k.a modules in python

# Playing with strings

print("Hello World")
print(" _______")
print("|       |")
print("|       |")
print("---------")


name = "tom"
age = "14"

print("The name is "+name)
print("The age is "+age)

name = "harry"
age = "7"
is_Male = True


print("The name is "+name)
print("The age is "+age)


print("This is a demo \n page")
print("This is a demo \" page")


phrase1 = "Laato ke bhoot"
phrase2 = "Baaton se nahi maante"

print(phrase1+phrase2) # Concatenation


# Working with basic string functions

print(phrase2.upper())  # Convert all lower case characters to upper
print(phrase2.isupper())  # TO check if the string is upper or not. Prints True or False
print(phrase2.upper().isupper()) # Convert all lower case characters to upper and check the casing immediately
print(len(phrase2))    # Calculate Length
print(phrase2[0])      # Printing value at index
print(phrase1.index("oo"))  # Printing where the argument starts
print(phrase2.replace("maante", "jaante"))  # Replace words or letters


# Playing around with numbers

print(-2)
print(2)
print(2+2)
print((3*4)+5)
print(10 % 3)

# Working with number functions

num1 = 5
num2 = -5
print(str(num1)+phrase2)  # Print number as a string, cuz printing number along with string requires it to be converted
print(num1.__add__(7))  # add number via function
print(abs(num2))  # Print the absolute value
print(pow(5, 2))  # 5^2
print(max(4, 8))  # maximum of the given numbers
print(min(4, 8))  # minimum  of the given numbers
print(round(3.02))  # rounding of to the nearest round figure
print(round(30.50))  # rounding of to the nearest round figure
print(round(3.92))  # rounding of to the nearest round figure

# We imported math function after this

print(floor(30.50))  # Print the floor value
print(ceil(30.50))   # Print the ceil value
print(sqrt(36))  # Print the square root of the provided number























