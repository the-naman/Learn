# Python 3 has 5 sequence types built in:
# • The string type
# . list
# • tuple
# • bytes and bytearray

# Sequence : A sequence is defined as an ordered set of items.

#All Sequence can not be multiplied or concatenated. Ex. range()


#STR Concatination
st1 = "He's "
st2 = "probably "
st3 = "pining"
st4 = "for the "
st5 = "Jordans."

print("He's " "probably " "pining" "for the " "Jordans.")
print(st1 + st2 + st3 + st4 + st5)


#STR multiplication
stt1 = "hello "
print(stt1 * 5)

# print(stt1 * 5 + 4)

print(stt1 * (5+4))

print(stt1 * 5 + "4")

# IN use in STR

d1 = "friday"
print("day" in d1)
print("fri" in d1)
print("thur" in d1)
print("wed" in d1)
