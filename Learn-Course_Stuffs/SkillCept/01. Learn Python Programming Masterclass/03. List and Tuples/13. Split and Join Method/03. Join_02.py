flowers = [
    "Daffodil", 
    "Evening Primrose", 
    "Hydrangea", 
    "Iris", 
    "Lavender", 
    "Sun Flower", 
    "Tiger Lily"
]

line = "=" * 40

print("Without Join (Iterrating list's items)")
print(line)
for flower in flowers:
    print(flower)

print("\n")

print("With join")
print(line)
print(", ".join(flowers))

print("\n")

print("With join and |")
print(line)
separator = " | "
output = separator.join(flowers)
print(output)

print("\n")
