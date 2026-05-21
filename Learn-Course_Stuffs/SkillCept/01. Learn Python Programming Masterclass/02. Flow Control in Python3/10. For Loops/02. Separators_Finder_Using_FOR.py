numbers = "9, 325; 223: 372 036, 854;775"
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators =   separators + char
print(separators)