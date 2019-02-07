# Playing around with files


# Reading a File
employee_file = open("employees.txt", "r")  # open()-> open file r-> read, w-> write, a-> append, r+ -> read and write

print(employee_file.readable())  # Gives status whethr the file is readable or not, can be replaced with write,etc

# print(employee_file.read())  # Prints the entire data.

# print(employee_file.readline())  # Prints the individual line op: giri - ceo
# print(employee_file.readline())  # op: ghan - cto

# print(employee_file.readlines())  # Will print in array format


for employee in employee_file.readlines():  # Will print results via for loop
    print(employee)


employee_file.close()


# Writing to a file and appending to a file
# employee_file = open("employees.txt", "W")  This will write to the file by overwriting the existing data

employee_file = open("employees.txt", "a")  # This will append to existing data

employee_file.write("\n"+"Anir - HR")

employee_file.close()

employee_file = open("employees1.txt", "w")  # This file did not exist at first but when we executed the code, a new
# file was created in the local folder.

employee_file.write("Terry - Defender")

employee_file.close()
