print("-" * 80)

if 0:
    print("True")
else:
    print("False")

print("-" * 80)

name = input("Please enter your name: ")

if name:
    print("Hello, {}".format(name))
else:
    print("Are you person with no name?")

print("-" * 80)

name2 = input("Please enter your Name: ")

if name2 != "":
    print("Hello, {}".format(name))
else:
    print("Are you person with no name?")
