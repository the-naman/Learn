def _is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

string_input = input("Enter word to check Palindrome: ")

while len(string_input) > 1:

    if _is_palindrome(string_input):
        print("'{}', is a Palindrome word.".format(string_input))
        break

    else:
        print("'{}', is not a Palindrome word.".format(string_input))
        break

else:
    print("No Input")