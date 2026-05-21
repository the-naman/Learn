# List : 
#     1. Lists are used to store multiple items in a single variable.
#     2. one of 4 built-in data types in Python
#     3. Lists are created using square brackets [].
#     4. List items are:-
#             i. ordered,                 : If you add new items to a list, the new items will be placed at the end of the list.
#             ii. changeable, and         : we can change, add, and remove items in a list after it has been created.
#             iii. allow duplicate values.: Since lists are indexed, lists can have items with the same value
#     5. List Length : determine how many items a list has, use the len() function
#             i. Syntax : print(len(thislist))
#     6. List Items - Data Types : List items can be of any data type (str, int, bool).
#     7. type() : lists are defined as objects with the data type 'list'
#             i. Syntax : print(type(mylist))
#     8. list() Constructor : to make a List : l1 = list(())


bag = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]
for item in bag:
    print(item)

print("-" * 80)

bag = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]
for i in bag:
    if i != "Nut":
        print(i)

print("-" * 80)

bag = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]
for j in bag:
    if j != "Nut":
        print(j)

print("-" * 80)