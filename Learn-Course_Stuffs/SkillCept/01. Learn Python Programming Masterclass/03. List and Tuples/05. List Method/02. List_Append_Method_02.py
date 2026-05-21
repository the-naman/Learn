current_choice = "-"
computer_parts = []         #empty list created

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("Computer")
            print("Computer Part Added: ", computer_parts)
        elif current_choice == "2":
            computer_parts.append("Monitor")
            print("Computer Part Added: ", computer_parts)
        elif current_choice == "3":
            computer_parts.append("Keyboard")
            print("Computer Part Added: ", computer_parts)
        elif current_choice == "4":
            computer_parts.append("Mouse")
            print("Computer Part Added: ", computer_parts)
        elif current_choice == "5":
            computer_parts.append("Mouse Pad")
            print("Computer Part Added: ", computer_parts)
        elif current_choice == "6":
            computer_parts.append("HDMI Cable")
            print("Computer Part Added: ", computer_parts)

    else:
        print("Please select the option to add item: ")
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: Mouse")
        print("5: Mouse Pad")
        print("6: HDMI Cable")
        print("0: Exit")

    current_choice = input("Enter your choice number: ")

else:
    print("Sucessfully Exit")

print("Final Computer parts: ", computer_parts)