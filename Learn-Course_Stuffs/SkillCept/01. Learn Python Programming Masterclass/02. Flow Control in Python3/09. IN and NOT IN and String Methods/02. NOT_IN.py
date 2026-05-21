# NOT IN : it is used to check that the given letter or sequence of char is not included / present in the available sequence.

word = "'The quick brown fox'"

letter = input("Enter the letter: ")

if letter not in word:
    print("{} not in {}".format(letter, word))

else:
    print("{} in the {}...... Please try again to check what not included".format(letter, word))