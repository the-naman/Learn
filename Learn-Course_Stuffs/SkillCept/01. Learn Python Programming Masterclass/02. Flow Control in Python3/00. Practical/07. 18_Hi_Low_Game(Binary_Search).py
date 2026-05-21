import random

print("Welcome to the Hi-Low Game.")

low = 1
high = int(input("Please enter the upper range: "))

high += 1

ans = random.randint(low, high)

guess_counter = 0

while True:
    guess = int(input("Enter your guess between {} and {}: ".format(low, high)))
    guess_counter += 1
    guess = low + (high - low) // 2

    if guess == 0:
        print("Game Over. You chosen to quit.")
        break

    elif guess == ans:
        print("Congrats.... You guessed the correct answer as {} in {} attempt.".format(ans, guess_counter))
        break

    elif guess != ans:
        if guess < ans:
            low = guess + 1
            print("Guess Higher...")

        elif guess > ans:
            high = guess -1
            print("Guess Lower")