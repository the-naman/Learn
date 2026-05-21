def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()

words = input("Enter your sentence or word to check palindrome: ")

if len(words) > 1:
    if palindrome_sentence(words):
        print("'{}', is Palindrome.".format(words))
    else:
        print("'{}', is not a Palindrome.".format(words))

else:
    print("No Input")