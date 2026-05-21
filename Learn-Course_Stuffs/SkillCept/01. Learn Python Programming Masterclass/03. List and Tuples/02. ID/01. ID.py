# id :
#     1. sytax : id()
#     2. id() is a built-in function that returns the unique identity of an object.
#     3. guaranteed to be unique and constant for that object during its lifetime. 

result = True
another_result = result
print(id(result))
print(id(another_result))
print("")

result1 = True
another_result1 = result1
print(id(result1))
print(id(another_result1))
result1 = False
print(id(result1))
print("")

result2 = "Correct"
another_result2 = result2
print(id(result2))
print(id(another_result2))
print(id(result2))
print("")

result2 += "ing"
print(id(result2))