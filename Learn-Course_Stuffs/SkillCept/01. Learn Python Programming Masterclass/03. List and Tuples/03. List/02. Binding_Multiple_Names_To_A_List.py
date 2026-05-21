shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

print(id(shopping_list))
print(shopping_list)
print("")

another_list = shopping_list
print(id(another_list))
print(another_list)
print("")

a = b = c = d = e = f = another_list

print("-----Printing a--------")
print(id(a))
print(a)
print("")

print("-----Adding 'Cream'--------")
b.append("Cream")
print(id(b))
print(b)
print("")

print("-----Printing c--------")
print(id(c))
print(c)