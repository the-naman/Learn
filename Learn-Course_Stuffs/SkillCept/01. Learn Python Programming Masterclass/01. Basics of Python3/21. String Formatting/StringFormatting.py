for i in range(1,13):
    print("Number {0}, Square is {1}, and Cube is {2}".format(i, i**2, i**3))

#space or left alignment
for i in range(1,13):
    print("Number {0:2}, Square is {1:3}, and Cube is {2:4}".format(i, i**2, i**3))

#right alignment
for i in range(1,13):
    print("Number {0:<2}, Square is {1:<3}, and Cube is {2:<4}".format(i, i**2, i**3))

#Center alignment
for i in range(1,13):
    print("Number {0:^}, Square is {1:^}, and Cube is {2:^6}".format(i, i**2, i**3))

print()

print("{0} is the value of (22/7) without width and precision.".format(22/7))
print()
print("{0:12f} is the value of (22/7) without 12 width and precision.".format(22/7))
print()
print("{0:12.50f} is the value of (22/7) without 12 width and 50 precision.".format(22/7)) # but 12 width ignored due to 50 precision
print()
print("{0:52.50f} is the value of (22/7) without 52 width and precision.".format(22/7))
print()
print("{0:62.50f} is the value of (22/7) without 62 width and 50 precision.".format(22/7))
print()
print("{0:72.50f} is the value of (22/7) without 72 width and 50 precision.".format(22/7))
print()
print("{0:<72.50f} is the value of (22/7) without 72 width and 50 precision.".format(22/7))
print()
print("{0:<72.54f} is the value of (22/7) without 72 width and 54 precision.".format(22/7))
