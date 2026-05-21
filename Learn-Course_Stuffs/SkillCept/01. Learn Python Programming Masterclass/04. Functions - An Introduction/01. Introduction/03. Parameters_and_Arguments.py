# Parameters : Are like placeholders for the rea values that you pass to the function (aka: formal parameters)
# Arguments : Are the value that will be used by formal parameters, when we call funtion. 

line = "=" * 80

print("Function Defining")
print(line)

def multiply(x, y):
    result = x * y
    return result

print()

print("Product of '10.5 and 4'")
print(line)
print(multiply(10.5, 4))

print()

print("Product of '6 and 7'")
print(line)
print(multiply(6, 7))

print()

print("Table of : 2")
print(line)
for i in range(1, 11):
    print(multiply(2, i))