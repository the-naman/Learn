# in reverse slicing :
# [start:stop:step]
# by default step size = 1
# the if we give any start value with -sign
# then it will print from that value to last character in that string

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters)

#last 4
print(letters[-4:])

#last 1
print(letters[-1:])

#from b to last
print(letters[1:])

#a
print(letters[:1])
print(letters[0])
