# Working with if statements and comparisons

def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:  # used comparison operator
        # print("num 1 is greatest")
        return num1
    elif num2 >= num1 and num2 >= num3:  # used comparison operator
        # print("num2 is the largest")
        return num2
    else:  # No need of comparison
        # print("num3 is the largest")
        return num3

numb1 = input("Input the first num")
numb1 = int(numb1)  # Converted text to int
numb2 = input("Input the second num")
numb2 = int(numb2)  # Converted text to int
numb3 = input("Input the third num")
numb3 = int(numb3)  # Converted text to int

print(max_num(numb1, numb2, numb3))


# Comparing strings

st1 = "Giridhar"
st2 = "Shenoy"

def max_string (str1, str2):
    if str1>=str2:
        return str1
    else:
        return str2


print(max_string(st1, st2))
