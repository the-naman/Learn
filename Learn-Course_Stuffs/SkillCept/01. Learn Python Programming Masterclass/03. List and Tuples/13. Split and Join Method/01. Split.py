panagram = "The quick brown fox jumps over the lazy dog"


# -- Statement :
print("Case 01: ")
print("Statement: ", panagram)

# -- Words split : 
print("\nCase 02: ")
print("Spliting words from statement: ", end = '')
words = panagram.split()
print(words)

# -- Splitting char from words : 
print("\nCase 03: ")
print("Spliting char from words: ", end = '')
for word in words:
    for char in word:
        print(char, end= ', ')
print()
# -- Panagram in multiple line with same view of space using """ """
print("\nCase 04: ")
panagram1 = """The quick brown
fox jumps\tover
the lazy dog"""
print("Another multiline statement: \n{}".format(panagram1))
print()

words1 = panagram1.split()
print("Word split from multiline statement: {}".format(words))
print()

print("Splitting char from word of multiline statement:", end=' ')
for word in words1:
    for c in word:
        print(c, end=', ')



# -- Split with numbers
print("\nCase 05: ")
num = "9 223 372 036 854 775 807"
num_list = num.split()
print("num: {}\n".format(num))

print("Splitted Numbers: {}\n".format(num_list))


# -- Challange to convert from all number from str to int
print("\nCase 06: ")
num = "9 223 372 036 854 775 807"
num_list = num.split()
print("num: {}\n".format(num))

print("Splitted Numbers in str: {}\n".format(num_list))
int_num_list = []
print("Solution 01:")
for i in num_list:
    int_num_list.append(int(i))

print("int_num_list: ", int_num_list, "\n")
print("Type of numbe in int_num_list: ", type(int_num_list[0]), "\n")

print("Solution 02:")
for index in range(len(num_list)):
    num_list[index] = int(num_list[index])
print("int numbers: ", num_list, "\n")

