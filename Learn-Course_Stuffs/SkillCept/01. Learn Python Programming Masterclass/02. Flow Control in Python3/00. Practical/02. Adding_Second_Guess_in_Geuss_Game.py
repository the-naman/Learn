ans = 5

print("Gues number between 1 to 10.")
guess = int(input("Enter your guess: "))

if guess > ans:
    print("Guess lower number.")
    guess2 = int(input("Gues number between 1 to 10."))
    if guess2 == ans:
        print("You guessed right, congo...")
    else:
        print("You did wrong again")

elif guess < ans:
    print("Guess higher number")
    guess2 = int(input("Gues number between 1 to 10."))
    if guess == ans:
        print("You guessed right, congo...")
    else:
        print("You did wrong again")

else:
    print("You did the right guess.")