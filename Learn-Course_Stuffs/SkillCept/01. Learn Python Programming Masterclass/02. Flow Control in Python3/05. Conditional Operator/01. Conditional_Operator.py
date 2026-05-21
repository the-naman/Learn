# Conditional Operators (ALL USED TO COMPARE AND CHECK) are as below:
#     1. Less Than                : <
#     2. Less Than or Equal to    : <=
#     3. Greater Than             : >
#     4. Greater Than or Equal to : >=
#     5. Equal to Equal to        : ==
#     6. Not Equal to             : !=


ans = 5

guess = int(input("Enter the number between 1 to 10."))

if guess != ans:
    if guess < ans:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Enter the number again... from 1 to 10."))
    if guess == ans:
        print("You guessed in second attempt, kudo..")
    else:
        print("Ahh... again you missed it.")
else:
    print("Congrats... You guessed in first attempt.")