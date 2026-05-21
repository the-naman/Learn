age = int(input("Enter your age?\n"))

if age >= 18 and age <= 60:
    print("You are eligible to both and Work.")
else:
    print("Enter the age in range (18-60).")

print("-" * 80)

if age < 18 or age > 60:
    print("Enjoy your time and memories.")
else:
    print("DO your best")