print("{} Concept Part {}".format("-"*20, "-"*20))
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


id = 1
for meal in menu:
    if "spam" in meal:
        print("List ", id, " in whole MENU contains word SPAM, and SPAM count= {}".format(meal.count("spam")))
        id += 1
    else:
        print("List ", id, " in whole MENU does not contains word SPAM")
        id += 1
print("{} Concept Part Ended. {}".format("-"*20, "-"*12))

print("")   # -----------------------------------------------------------------------------------------------------

print("{} Challenge Part {}".format("-"*20, "-"*20))
menu_list = [
    ["egg", "bacon"], 
    ["egg", "sausage", "bacon"], 
    ["egg", "sweets"], 
    ["egg", "bacon", "sweets"], 
    ["egg", "bacon", "sausage", "sweets"], 
    ["sweets", "bacon", "sausage", "sweets"], 
    ["sweets", "sausage", "sweets", "bacon", "sweets", "tomato", "sweets"], 
    ["sweets", "egg", "sweets", "sweets", "bacon", "sweets"], 
]

index = 1
for item in menu_list:
    if "spam" in item:
        print("List {} contains word SPAM, and count is: {}".format(index, item.count("spam")))
    else:
        print("List {} does not contains word 'SPAM'.".format(index))
    index += 1
print("{} Challenge Part Ended. {}".format("-"*20, "-"*12))