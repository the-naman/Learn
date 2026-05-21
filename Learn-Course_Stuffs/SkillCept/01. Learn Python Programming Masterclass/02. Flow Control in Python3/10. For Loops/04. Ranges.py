# Range : Create a sequence of numbers from start value to [last value - 1].
# Syntax : range(start, stop, step) 

for i in range(1,21):
    print("Now number is {}".format(i))

print("_" * 80)

for j in range (10):
    print("Current number is {}".format(j))

print("_" * 80)

for k in range(2, 11, 2):
    print("Current number is {}".format(k))

print("_" * 80)

for n in range (10, 0, -2):
    print("Current num is {}".format(n))

print("_" * 80)

# Age problem solution
# if age from 18 to 60 you are eligible to vote and work.
# if below than 18 then create memories and If older than 60 then enjoy your rest of life

age = int(input("Enter your current age: "))

if age in range(18, 61):
    print("Your are eligible to Vote and Earn.")
elif age in range(0,18):
    print("Create Memories.")
elif age in range(61, 111):
    print("Enjoy Life")
else:
    print("Out of range input")

print("_" * 80)

