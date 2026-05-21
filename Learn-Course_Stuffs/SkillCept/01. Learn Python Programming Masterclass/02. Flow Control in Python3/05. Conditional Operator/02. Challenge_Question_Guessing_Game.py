ans = 5

guess = int(input("Enter the number between 1 to 10."))

if guess == ans:
    print("Congrats... You guessed in first attempt.")
    
else:
    if guess < ans:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Enter the number again... from 1 to 10."))
    if guess == ans:
        print("You guessed in second attempt, kudo..")
    else:
        print("Ahh... again you missed it.")