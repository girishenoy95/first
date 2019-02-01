# Playing with try/except bloc i.e similar to try catch block

# Example 1
try:
    number=int(input("Please enter a number"))
    print(number)
except:  # Will catch any exception  (Very Broad definition for except)
    print("Please input a int value")


# Example 2
try:
    di = 10/0
    print("Number divided by zero")
except ZeroDivisionError:   # Will catch a specific exception
    print("Cannot divide by zero")


# Example 3
try:
    di = 10/0
    print("Number divided by zero")
except ZeroDivisionError as err:  # Will store the error in a variable we can print via variable
    print(err)
