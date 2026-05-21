print("{} Horizontal List Method {}".format("-"*20, "-"*20))
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

for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

print("{} 1st Method Part Ended. {}".format("-"*20, "-"*12))

print("")

print("{} Vertical List Method {}".format("-"*20, "-"*20))

menu1 = [
    ["egg", "bacon"], 
    ["egg", "sausage", "bacon"], 
    ["egg", "spam"], 
    ["egg", "bacon", "spam"], 
    ["egg", "bacon", "sausage", "spam"], 
    ["spam", "bacon", "sausage", "spam"], 
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"], 
    ["spam", "egg", "spam", "spam", "bacon", "spam"], 
]

for meal in menu1:
    for item in meal:
        if meal == "spam":
            continue
        else:
            print(item)
    print()

print("{} 2nd Method Part Ended. {}".format("-"*20, "-"*12))