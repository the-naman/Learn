# IN : it is used to check the character or letter or anything in the given sequence.

animal = "Lion"

letter = input("Enter your char/ letter to check in Sequence: ")

if letter in animal:
    print("{} is in {}".format(letter, animal))
else:
    print("Nope, this given letter is not is the word.")