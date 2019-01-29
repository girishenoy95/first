# Building a guessing game

word = "phonepe"
guess = ""
i = 0

while guess != word and i <= 4:
    guess = input("Enter the word ")
    i += 1

if guess == word:
    print("You Win")
else:
    print("Loser Bitch")
