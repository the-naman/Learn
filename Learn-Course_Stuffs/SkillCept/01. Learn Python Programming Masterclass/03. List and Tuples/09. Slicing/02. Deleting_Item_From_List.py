data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

#code 01:
print("-"*20, "CODE 01", "-"*20)

print(data)

del data[:2]
print(data)

print("-"*20, "CODE 01 END", "-"*16)
print()

#code 02:
print("-"*20, "CODE 02", "-"*20)

print(data)

del data[16:]
print(data)

print("-"*20, "CODE 02 END", "-"*16)
print()

#code 03:
print("-"*20, "CODE 03", "-"*20)

print(data)

del data[14:]
print(data)


print("-"*20, "CODE 03 END", "-"*16)
print()

#code 04:
print("-"*20, "CODE 04", "-"*20)

data1 = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

valid_min = 100
valid_max = 200

for index, value in enumerate(data1):
    if (value < valid_min) or (value > valid_max):
        print("'Value': ", value, " and 'index': ", index)
        del data1[index]
        print(data1)

# Note : this code left out some value to delete and moved ahead, so this code is wrong means not a good solution.
#        In next python file solution is.

print("-"*20, "CODE 04 END", "-"*16)
print()