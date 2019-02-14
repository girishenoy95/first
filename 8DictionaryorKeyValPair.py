# Playing around with Dictionary

# It is basically key value pair


monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June"
}

print(monthConversion["Mar"])  # One way to access value via Key
print(monthConversion.get("Feb"))  # Another way to access value via Key

print(monthConversion.get("NaK", "Not a Key in the dictionary"))  # print a default value when the key is not specified


# Similarly when we have key as numbers and values as pair

monthConversion_new = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June"
}


print(monthConversion_new[1])  # One way to access value via Key
print(monthConversion_new.get(1))  # Another way to access value via Key




