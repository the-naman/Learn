# Slicing:
    # 1. It is a way to get specific parts of a string by using start, end and step values.
    # 2. It’s especially useful for text manipulation and data parsing.

#Syntax :
    # substring = s[start(optional) : end(optional) : step(optional)]

# Negative slicing :
    # 1. It is used to access elements from the end of a sequence.
        # -1: refers to the last element.
        # -2: refers to the second-to-last element, and so on.
        # The index -len(sequence) refers to the first element.

# Code 01:
computer_parts = [
    "Computer", 
    "Monitor", 
    "Keyboard", 
    "Mouse", 
    "Mouse Pad"
]

print(computer_parts)           # print wwhole list
print()

print(computer_parts[3:])       # print from index 3 to 4
print()

computer_parts[3:] = "TrackBall"
print(computer_parts)
print()

computer_parts[3:] = ["TrackBall"]
print(computer_parts)
print()