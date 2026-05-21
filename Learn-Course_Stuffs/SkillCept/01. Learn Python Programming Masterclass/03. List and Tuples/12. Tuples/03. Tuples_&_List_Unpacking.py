# Case 01:
print("Case 01: Assigning same value to multiple variable at same line.\n")

a = b = c = d = e = f = 42
print("Syntax or code: a = b = c = d = e = f = 42")
print("Printing value using 'a' variable", a)
print("Printing value using 'e' variable", e)

# Case 02:
print("\nCase 02: Normal unpacking\n")

x, y, z = 67, 35, 29
print("x, y, z, values", x, y, z)
print("X value", x)
print("Y value", y)
print("Z value", z)

# Case 03:
print("\nCase 03: Tuple unpacking\n")

data = 75, 45, 23
x, y, z = data
print("Data: ", data)
print("X value", x)
print("Y value", y)
print("Z value", z)

# Case 04:
print("\nCase 04: List unpacking\n")

data_list = [73, 58, 71]
p, q, r = data
print("Data_List: ", data_list)
print("P value", p)
print("Q value", q)
print("R value", r)

# Case 05:
print("\nCase 05: Tuple Unpacking using enumerate.\n")

print("Data: ABCDEFGH")
for d in enumerate("ABCDEFGH"):
    index, char = d
    print("Index= {}, Value= {}".format(index, char))

# Case 06:
print("\nCase 06: Tuple Unpacking using enumerate in another view.\n")

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

name_list = [welcome, bad, budgie, imelda, metallica]
option_list = ["Welcome", "Bad", "Budgie", "imelda", "Metallica"]
valid_choice = []
for i in range(1, len(option_list)+1):
    valid_choice.append(i)
choice = 999999999999999999999999999999999999999999999999

try:
    while choice > 0:
        if choice in valid_choice:
            title, artist, year = name_list[choice-1]
            print("Title:  ", title)
            print("Artist: ", artist)
            print("Year:   ", year)
    
        else:
            print("Choose desired option: ")
            for id, val in enumerate(option_list):
                print("{}. {}".format(id+1, val))
            print("0. Exit")
        choice = int(input("Enter your choice: "))
    else:
        print("Exit successfull")
except:
    print("Invalid Try..... Run again..")