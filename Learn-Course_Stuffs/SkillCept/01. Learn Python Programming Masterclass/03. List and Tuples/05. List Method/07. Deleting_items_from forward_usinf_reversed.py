data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

top_index = len(data) - 1
rval_item = []
final_list = []


for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        rval_item.append(value)

for i in data:
    if i not in rval_item:
        final_list.append(i)

print("Original List: ", data)
print("Non-valid items in the original list (value < 100 or value > 200): ", rval_item)
print("Final list after removal of non-valid items: ", final_list)