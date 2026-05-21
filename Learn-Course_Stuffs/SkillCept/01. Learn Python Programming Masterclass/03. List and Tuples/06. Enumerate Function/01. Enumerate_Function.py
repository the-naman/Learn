# The enumerate() function in Python is a built-in function that 
# adds a counter to an iterable and returns it as an enumerate object. 
# This object can then be used in loops to access both the index and 
# the value of each item in the iterable simultaneously



# Advantages of enumerate():

#     Cleaner code:
#     It provides a more concise and readable way to access both the index and value during iteration compared to manually managing a counter variable.
#     No need for manual indexing:
#     It eliminates the need to initialize a counter and increment it within the loop.
#     Efficiency:
#     As a built-in function, enumerate() is generally optimized for performance.


# Syntax : enumerate(list_name, index_start_number=(Optional))


#CODE 1:
print("-"*80)
print("Code - 01")

fruits = ["Banana", "Kiwi", "Apple", "Mango", "Lichi", "Grapes"]
print("List of fruits are: ")
for index, fruit in enumerate (fruits):
    print("{0}. {1}".format((index+1), fruit))
print("-"*80)

#CODE 2:
print("-"*80)
print("Code - 02")

players = ["Yuvraj", "Dhoni", "Rohit", "Kohli"]
for number, name in enumerate(players, start=1):
    print("{}. {}".format(number, name))
print("-"*80)

#CODE 3:
print("-"*80)
print("Code - 03")

students = ["Shashank", "Madhvan", "Rohit", "Sumit"]
for index, name in enumerate(students):
    print("index= {}, and, name= {}".format(index, name))
print("-"*80)
