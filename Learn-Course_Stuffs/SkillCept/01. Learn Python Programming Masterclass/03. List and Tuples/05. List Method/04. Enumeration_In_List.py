available_computer_parts = ["Computer", "Monitor", "Web Cam", "Keyboard", "Mouse", "HDMI Cable"]
current_choice = "-"
computer_parts_cart = []         #empty list created

# Gathering indexes from available parts list
valid_choice = []
for i in range (1, len(available_computer_parts)+1):
    valid_choice.append(str((i)))

# Comparing current choice to perform operations
while current_choice != '0':
    if current_choice in valid_choice:
        index = int(current_choice) -1
        chosen_part = available_computer_parts[index]

        # Code to remove chosen parts
        if chosen_part in computer_parts_cart:
            print("Removing {}".format(current_choice))
            print("'{}' Removed.".format(chosen_part))
            computer_parts_cart.remove(chosen_part)

        #Code to add item in cart
        elif chosen_part not in computer_parts_cart:
            print("Adding {}".format(current_choice))
            computer_parts_cart.append(chosen_part)
            print("'{}' Added.".format(chosen_part))

    # Printing out list of available items in the list of market
    else:
        print("Please select the option to add item: ")
        for number, part in enumerate(available_computer_parts):
            print("{0}: {1}".format(number+1, part))
        print("0: Exit")
        

    current_choice = input("Enter your choice number: ")

# printing only on exit 
else:
    print("Sucessfully Exit")

print("Final Computer parts: ", computer_parts_cart)