import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # elif not temp.isnumeric():
        print("'{}' is an Invalid Input".format(temp))
        


high = get_integer("Enter the highest value you want: ")

ans = random.randint(1, (high+1))

print("Please guess a number between '1' and '{}'.".format(high), "ans= ", ans)

guess_counter = 0

while True:
    guess = get_integer("Please enter your guess integer: ")
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