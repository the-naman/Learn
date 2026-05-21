# Guessing Game

answer = 5

guess = int(input("Enter number between 1 to 10: "))

if guess < answer:
    print("Please guess higher.")
elif guess > answer:
    print("Please guess lower.")
else:
    print("You guessed right.")