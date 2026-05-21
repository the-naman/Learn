# Break : Used to break the current for or while loop and move to next loop.

item_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Nut"
item_found_at = None            # (None : None represents Nothing and of none data type)

for index in range(len(item_list)):
    if item_list[index] == item_to_search:
        item_found_at = index
        break
    
print("Item found at {}".format(item_found_at))