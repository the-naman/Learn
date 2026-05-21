# Operator Precedance
a = 12
b = 3

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print( ( ( ( a + b ) / 3 ) - 4 ) * 12 )
print((( a + b ) / 3 - 4) * 12)

print()

c = a+b
d = c/3
e = d-4
f = e*12
print(f)

print(a/(b*a)/b)