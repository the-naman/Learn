import random

high = int(input("Enter the highest value you want: "))

ans = random.randint(1, (high+1))
print(ans)

guess_counter = 1

while True:
    guess = int(input("Please enter your guess integer: "))
    guess_counter = guess_counter + 1

    if guess == 0:
        print("You chosen to quit. GAME OVER!!")
        break

    elif guess == ans:
        print("Congrats you guessed it successfully in {} attempt".format(guess_counter))
        break

    elif guess != ans:
        if guess < ans:
            print("Guess Higher...")

        elif guess > ans:
            print("Guess Lower....")