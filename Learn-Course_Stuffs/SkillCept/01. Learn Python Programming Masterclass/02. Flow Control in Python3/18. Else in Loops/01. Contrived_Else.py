numbers = [1, 3, 5, 40, 52, 60]

for num in numbers:
    if num % 8 == 0:
        print("List's numbers are Unacceptable.")          # Here rejecting multiple of 8 numbers
        break
    
else:
    print("All numbers are fine of the list.")              # This else will run only when for loop not run