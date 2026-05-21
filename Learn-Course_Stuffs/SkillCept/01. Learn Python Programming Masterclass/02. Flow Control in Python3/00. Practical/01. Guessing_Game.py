ans = 5

print("Gues number between 1 to 10.")
guess = int(input("Enter your guess: "))

if guess > ans:
    print("Guess lower number.")

elif guess < ans:
    print("Guess higher number")

else:
    print("You did the right guess.")