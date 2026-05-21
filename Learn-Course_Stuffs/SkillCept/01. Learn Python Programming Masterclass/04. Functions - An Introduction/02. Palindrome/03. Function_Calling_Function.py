def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)
line = "=" * 40


while True:
    words = input("0. To get Exit.\n" 
    "Enter your sentence or word to check palindrome: ")

    if len(words) <= 0:
        print("No Input")

    elif len(words) > 1:
        if palindrome_sentence(words):
            print("'{}', is Palindrome.".format(words), "\n", line, "\n")
        
        else:
            print("'{}', is not a Palindrome.".format(words), "\n", line, "\n")
            

    elif int(words) == 0:
        print("Exit")
        break
        