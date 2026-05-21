#Negative index means it count from last to start/first.
# last character index will be -1 not 0




#           1
#      -(43210987654321)                
p_str = "Norwegian Blue"

print(p_str)
print()
print(p_str[-11])
print(p_str[-10])
print(p_str[-5])
print(p_str[-11])
print(p_str[-8])
print(p_str[-6])
print()
# another version to do negative indexing
# last index = -14
# actual index = positive index - last index


#           1
#      -(43210987654321)                
p_str = "Norwegian Blue"
#       (01234567890123)
#                  1
print(p_str)
print()
print(p_str[3-14])
print(p_str[4-14])
print(p_str[9-14])
print(p_str[3-14])
print(p_str[6-14])
print(p_str[8-14])