# Case 01:
print("Case 01: \n")

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print("Metallica: ", metallica)
print("Metallica[0]: ", metallica[0])
print("Metallica[1]: ", metallica[1])
print("Metallica[2]: ", metallica[2])

# Case 02: 
print("\nCase 02: Assigning other value to an index of mettlica... \n")

try :
    metallica[0] = "Master of Puppets"
except:
    print("Giving :", TypeError)

# Case 03: 
print("\n\nCase 03:Converting a tuple into a list \n")
metallica_list = list(metallica)
print("Metallica in list form: ", metallica_list)

print("\nPrinting value of metallica from list created...")
print("Metallica[0]: ", metallica_list[0])
print("Metallica[1]: ", metallica_list[1])
print("Metallica[2]: ", metallica_list[2])


# Case 04: 
print("\nCase 04: Assigning other value to Mettalica list index = 0")
print("Older Metallica List: ", metallica_list)
metallica_list[0] = "Master of Puppets"
print("Updated Metallica List: ", metallica_list)

print()