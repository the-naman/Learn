data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# Code 01:
print("-"*20, "CODE 01: Lower Removal", "-"*20)

print("Data List", data)
print("Data lower than: ", min_valid)
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print("Data removing: ", data[:stop])
print("'Index or Stop point': ", index, " and 'Nearest High Value': ", value)
del data[:stop]
print("List after min value removal: ", data)

print("-"*20, "CODE 01 END", "-"*16)
print()

# ---------------------------------------------------------------------------------------------------------------

data1 = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 200, 350, 360]

min_valid = 100
max_valid = 200

# Code 02:
print("-"*20, "CODE 02 : Higher Removal", "-"*20)

print("Data List", data1)
print("Data equal to or higher than: ", max_valid)
start = 0
for index, value in enumerate(data1):
    if value >= max_valid:
        start = index
        break
print("Data removing: ", data1[start:])
print("'Index or Start point': ", index, " and 'Nearest High Value': ", value)
del data1[start:]
print("List after min value removal: ", data1)

print("-"*20, "CODE 02 END", "-"*16)
print()