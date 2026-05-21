name = str(input("Enter your name :"))
age = int(input(f"Enter your age, {name} :"))

if age < 18:
    print(f"Come after {18-age} years.")
elif age > 18:
    print("Eligible to vote.")
else:
    print("Run Complete")