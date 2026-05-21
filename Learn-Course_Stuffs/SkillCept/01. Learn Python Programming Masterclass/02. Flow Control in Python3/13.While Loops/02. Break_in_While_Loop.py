exit_gate = ["East", "West", "North", "South"]

chosen_exit_gate = ""

while chosen_exit_gate not in exit_gate:
    chosen_exit_gate = input("Please choose the exit Gate: ")
    if chosen_exit_gate.casefold() == "quit":
        print("Game Over")
        break

print("Aren't you glad you got out of there?")

# TODO : remove 1