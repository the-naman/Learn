# What if we give a tab indentation to the last print?
# Ans : It will print after every line.

for i in range(1,5):
    for j in range(1,5):
        print("{} times {} is {}".format(j, i, i*j))

        print("-" * 40)

print("-" * 100)

# What if we remove all indentation of the last print?
# Ans : It will print only at last

for i in range(1,5):
    for j in range(1,5):
        print("{} times {} is {}".format(j, i, i*j))

print("-" * 40)