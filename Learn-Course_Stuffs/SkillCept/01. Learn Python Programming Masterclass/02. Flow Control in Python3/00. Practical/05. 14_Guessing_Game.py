import random

highest = int(input("Enter the highest number you want for the range: "))

ans = random.randint(1, highest+1)

guess = int(input("Guess the number between 1 to {}: ".format(highest)))

if guess == ans:
    print("Kudos... You guessed it in First try.")
else:
    i = 1               # guess counter
    while guess != ans:
        if guess == 0:
            print("Successfully Quit")
            break
        elif guess > ans:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        i = i+1
        guess = int(input("Guess the number between 1 to {}: ".format(highest)))
    print("Kudos... You guessed it in {} attempt.".format(i))
