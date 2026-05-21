name = str(input("Enter your name : "))
age = int(input("Enter your age, {0} :".format(name)))

if age >= 18:
    print("Eligible to vote.")
    print("Apply for voter ID Card.")
else:
    print("Not eligible to vote.")
    print(f"Come after {18-age} years.")

if age < 18:
    print("Not eligible to vote.")
    print(f"Come after {18-age} years.")
else:
    print("Eligible to vote.")
    print("Apply for voter ID Card.")