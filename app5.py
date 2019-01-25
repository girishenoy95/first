# working with if else


# Working with or
is_Male = False
is_Tall = False


if is_Male or is_Tall:
    print("You are a male or tall or both")
else:
    print("You are not a male or tall or both")


# Working with and & elif (Elseif)
is_Male = True
is_Tall = False


if is_Male and is_Tall:
    print("You are a male and tall")
elif is_Male and not is_Tall:
    print("You are a male but not tall")
elif not is_Male and is_Tall:
    print("You are not a male but tall")
else:
    print("You are not a male and tall")



