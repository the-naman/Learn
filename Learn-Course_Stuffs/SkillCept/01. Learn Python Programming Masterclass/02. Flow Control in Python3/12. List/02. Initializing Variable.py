item_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Nut"
item_found_at = None            # (None : None represents Nothing and of none data type)

for index in range(len(item_list)):
    if item_list[index] == item_to_search:
        item_found_at = index
        break
    
print("Item found at {}".format(item_found_at))

print("-" * 80)                 # -----------------------------------------------------------------------------

item1_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Sweets"
item_found_at = None            # (None : None represents Nothing and of none data type)

for index in range(len(item1_list)):
    if item1_list[index] == item_to_search:
        item_found_at = index
        break
    
print("Item found at {}".format(item_found_at))

print("-" * 80)                 # -----------------------------------------------------------------------------

item2_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Sweets"
item_found_at = None            # (None : None represents Nothing and of none data type)

for index in range(len(item2_list)):
    if item2_list[index] == item_to_search:
        item_found_at = index
        break
if item_found_at is not None:
    print("Item found at {}".format(item_found_at))
else:
    print("{} not found.".format(item_to_search))

print("-" * 80)                 # -----------------------------------------------------------------------------

item3_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Ghee"
item_found_at = None            # (None : None represents Nothing and of none data type)

for index in range(len(item3_list)):
    if item3_list[index] == item_to_search:
        item_found_at = index
        break
if item_found_at is not None:
    print("Item found at {}".format(item_found_at))
else:
    print("{} not found.".format(item_to_search))

print("-" * 80)                 # -----------------------------------------------------------------------------

item4_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Sweets"
item_found_at = None            # (None : None represents Nothing and of none data type)

if item_to_search in item4_list:
    item_found_at = item4_list.index(item_to_search)

if item_found_at is not None:
    print("Item found at {} position.".format(item_found_at))
else:
    print("{} not found".format(item_to_search))

print("-" * 80)                 # -----------------------------------------------------------------------------

item5_list = ["Milk", "Butter", "Ghee", "Nut", "Curd", "Cheese"]

item_to_search = "Ghee"
item_found_at = None            # (None : None represents Nothing and of none data type)

if item_to_search in item5_list:
    item_found_at = item5_list.index(item_to_search)

if item_found_at is not None:
    print("Item found at {} position.".format(item_found_at))
else:
    print("{} not found".format(item_to_search))