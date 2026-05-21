menu = [
    ["egg", "bacon"], 
    ["egg", "sausage", "bacon"], 
    ["egg", "spam"], 
    ["egg", "bacon", "spam"], 
    ["egg", "bacon", "sausage", "spam"], 
    ["spam", "bacon", "sausage", "spam"], 
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"], 
    ["spam", "egg", "spam", "spam", "bacon", "spam"], 
]

line = "=" * 40
a1 = []
a2 = []
for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    a1.append(meal)
    a2.append(", ".join(meal))

print("Without join")
print(line)
for i in a1:
    print(i)

print("\n")

print("With join")
print(line)
for j in a2:
    print(j)