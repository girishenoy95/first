# This is one way of doing it

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

phr = "Dig Doggy Dogg"

print(translate(phr))  # Output will be Dgg Dgggy Dggg


# Another way that can be done using python
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation
phr = "Igloo"
print(translate(phr))  # Output for this will be Gglgg
