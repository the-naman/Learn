# Continue : It skip the current iteration of the loop to next iteration of the same loop.

for i in range (1, 11):
    if i == 7:
        continue
    print(i)

print("-" * 80)

bag = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]
for item in bag:
    if item != "Nut":
        print(item)

print("-" * 80)

bag1 = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]
for k in bag1:
    if k == "Nut":
        continue
    print(k)