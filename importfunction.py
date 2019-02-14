import random

feet_in_miles = 1000
meters_in_km = 1000
random_names = ["Randy orton", "Invisible", "Sheamus", "Shawn Michaels"]

def get_file_ext(filename):
    return filename[filename.index()+1]

def roll_a_die(num):
    return random.randint(1, num)


