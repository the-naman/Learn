line = "=" * 51

print("Returning Value\n", line)
def multiply(x, y):
    result = x * y
    return result

print("The product of 18 and 3 = {}\n\n".format(multiply(18, 3)))

print("Returning None\n", line)
def multiply(x, y):
    result = x * y
    # return result

print("The product of 18 and 3 = {}\n\n".format(multiply(18, 3)))