name = str(input("Enter your Name: "))
age = int(input("Enter your Age: "))

#age must be over 18 and under 31
if 18 <= age < 31:
    print("Holiday")
else:
    print("You can't")