#slicing : method to extract a sub string or parts from a whole string.
#syntax : [start:stop:step]

#                     1
#           012345678901234             #here 14 is the extra index for extracting character "e"
p_string = "Norwegian Blue"
print(p_string)
print()

#slice word "we"
print(p_string[3:5])
print()

#slice word "gian"
print(p_string[5:9])
print()

#slice word "Norwegian"
print(p_string[0:9])
print(p_string[:9])
print()

#slice word "Blue"
print(p_string[10:14])
print(p_string[10:])
print()

print(p_string[:6]) # it will printfrom start till index 5
print(p_string[6:]) # it will print from index 6 till last

print(p_string[:6] + p_string[6:])  # it wil print whole string

print(p_string[:])  #it will print whole string
