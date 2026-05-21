import random

print("Welcome to the Hi-Low Game.")

low = 1
high = int(input("Please enter the upper range: "))

high += 1

ans = random.randint(low, high)
print(ans)

guess_counter = 0
guess = int()

while guess != ans:
    guess = int(input("Enter your guess between {} and {}: ".format(low, high)))
    guess_counter += 1
    if guess == ans:
        print("Your number is {}.".format(ans))
        print("You guessed in {} attempt.".format(guess_counter))
        break

    elif guess == 0:
        print("Game Over. You chosen to quit.")
        break

    elif low <= guess <= high:
        
        guess = low + (high - low) // 2

        if guess != ans:
            if guess < ans:
                low = guess + 1
                print("Guess Higher...")

            elif guess > ans:
                high = guess -1
                print("Guess Lower")
    else:
        print("Invalid Input... Please try Again..")

else:
    print("Your number is {}.".format(ans))
    print("You guessed in {} attempt.".format(guess_counter))