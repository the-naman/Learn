def rever(data):
    """
    Get a string from user Standard Input (stdin) 
    The function will check the input is equal to reverse of itself or not?

    :param: It is the string that user will see when prompting the data
    Here data inpute type is `str`

    :return: 
    if input is reverse of itself, print YES, otherwise NO
    """
    if data[::-1].casefold() == data.casefold():
        print(str("YES, REVERSE"))
    else:
        print(str("Not Reverse"))
    

rever(input("Enter your text: "))