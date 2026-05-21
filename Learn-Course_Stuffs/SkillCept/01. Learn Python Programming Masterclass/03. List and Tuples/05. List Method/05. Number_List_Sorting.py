empty_list = []
print("Empty List:           ", empty_list)
print()

new_list = list()
print("Empty List:           ", new_list)
print()

even = [2,4,6,8]
print("Even number List:     ", even)
print()

odd = [1,3,5,7,9]
print("Odd number List:      ", odd)
print()

numbers = even + odd
print("Numbers List:         ", numbers)
print()

sorted_numbers = sorted(numbers)
print("Sorted number list:   ", sorted_numbers)
print()

digits = list("6735282197")
print("Digits List:          ", sorted(digits))
print()

another_number = list(numbers)
print("Another number list:  ", another_number)
print()

more_numbers = numbers[:]
print("More Numbers :        ", more_numbers)
print()

more_numbers_copied = numbers.copy()
print("More Copied Numbers : ", more_numbers_copied)
print()

# checkig same list or two different list containg same elements:
print("'Numbers is Another_Number': ", numbers is another_number)
print()

print("'Numbers == Another_Number': ", numbers == another_number)
print()

print("'Numbers is More_Numbers':   ", numbers is more_numbers)
print()

print("'Numbers == More_Numbers':   ", numbers == more_numbers)
print()

print("'Numbers is More_Numbers_Copied': ", numbers is more_numbers_copied)
print()

print("'Numbers == More_Numbers_Copied': ", numbers == more_numbers_copied)
print()