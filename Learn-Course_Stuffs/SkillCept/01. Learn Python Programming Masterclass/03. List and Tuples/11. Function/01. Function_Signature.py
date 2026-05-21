# Function Signature :
# Means     : 1. Definition of a function
#             2. That includes the function's name and the parameters that it defines

# Print function signature : print(*objects, sep=' ', end='\n', file=None, flush=False)

# Print case 01:
print("Case 01: ")

name = "Naman"
age = 25
location = "India"
print(name, age, location, 11011101, "Kumar")


# Print case 02: 
print("\nCase 02: ")
name = "Kumar"
age = 25
location = "India"
print(name, age, location, 11011101, "Naman", sep = ':  ')


# Print case 03: 
print("\nCase 03: ")


# Print case 04: 
print("\nCase 04: ")
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
            print(item, end = ', ')
    print()