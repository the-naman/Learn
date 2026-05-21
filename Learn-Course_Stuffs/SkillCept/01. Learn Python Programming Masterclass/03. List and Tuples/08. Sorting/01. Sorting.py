# Code 01
print("-"*20, "CODE 01", "_"*20)

pargam = "The quick brown fox jump over the lazy dog."
letters = sorted(pargam)
print(letters)

print("-"*20, "CODE 01 END", "_"*16)
print("\n")


#code 02
print("-"*20, "CODE 02", "_"*20)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print("NUmbers:", numbers)
print("Sorted Numbers: ", sorted_numbers)

print("-"*20, "CODE 02 END", "_"*16)
print("\n")



#code 03
print("-"*20, "CODE 03", "_"*20)

another_sorted_numbers = numbers.sort()
print("Numbers: ", numbers)
print("Another sorted numbers: ", another_sorted_numbers)

print("-"*20, "CODE 03 END", "_"*16)
print("\n")

#code 04
print("-"*20, "CODE 04", "_"*20)

missing_letters = "The quick brown fox jumped over the lazy dog."
print(sorted(missing_letters, key = str.casefold))

print("-"*20, "CODE 04 END", "_"*16)
print("\n")

#code 05
print("-"*20, "CODE 05", "_"*20)

missing_letters_2 = sorted("The quick brown fox jumped over the lazy dog." , key = str.casefold)
print(missing_letters_2)

print("-"*20, "CODE 05 END", "_"*16)
print("\n")

#code 06
print("-"*20, "CODE 06", "_"*20)

names = [
    "Piuysh",
    "Ritik",
    "Krishna",
    "Naman",
    "golu",
    "motu",
    "patlu"
]
names.sort()
print("Names Sorted without casefold: ", names)

names.sort(key = str.casefold)
print("Names Sorted with casefold: ", names)

print("-"*20, "CODE 06 END", "_"*16)
print("\n")
