numbers = input("Enter the numbers with separators: ")

sep = ""
num = ""
num1 = ""

for char in numbers:
    if char.isnumeric():
        num = num + char
    num1 = num

    if not char.isnumeric():
        sep = sep + char
print(sep)
print(num1)
