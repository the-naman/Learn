available_computer_parts = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse Pad", "HDMI Cable"]
current_choice = "-"
computer_parts_cart = []         #empty list created

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts_cart.append("Computer")
            print("Computer Part Added: ", computer_parts_cart)
        elif current_choice == "2":
            computer_parts_cart.append("Monitor")
            print("Computer Part Added: ", computer_parts_cart)
        elif current_choice == "3":
            computer_parts_cart.append("Keyboard")
            print("Computer Part Added: ", computer_parts_cart)
        elif current_choice == "4":
            computer_parts_cart.append("Mouse")
            print("Computer Part Added: ", computer_parts_cart)
        elif current_choice == "5":
            computer_parts_cart.append("Mouse Pad")
            print("Computer Part Added: ", computer_parts_cart)
        elif current_choice == "6":
            computer_parts_cart.append("HDMI Cable")
            print("Computer Part Added: ", computer_parts_cart)

    else:
        print("Please select the option to add item: ")
        for parts in available_computer_parts:
            print("{0}: {1}".format(available_computer_parts.index(parts)+1, parts))
        print("0: Exit")
        

    current_choice = input("Enter your choice number: ")

else:
    print("Sucessfully Exit")

print("Final Computer parts: ", computer_parts_cart)