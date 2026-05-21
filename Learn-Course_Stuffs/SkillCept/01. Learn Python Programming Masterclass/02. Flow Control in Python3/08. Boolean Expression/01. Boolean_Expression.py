# Boolean have two values : 
# True
# False

# And, NOT (not) is used to reverse the True as False and False as True
# Order Precedance (High to Low): NOT, AND, OR

print("-" * 80)

day = "Sat"
temp = 30
swimming = True

if day=="Sat" and temp > 27 and not swimming:     #(Yaha equation banega : True and True and False  --> True and False --> False )
    print("Go for swimming.")
else:
    print("Learn Python.")

print("-" * 80)

day1 = "Sat"
temp1 = 30
swimming1 = False

if day1 =="Fri" and temp1  > 27 or not swimming1:     #(Yaha equation banega : False and True or True  -->  False or True --> True )
    print("Go for swimming.")
else:
    print("Learn Python.")

print("-" * 80)

day2 = "Sat"
temp2 = 30
swimming2 = False

if (day2 =="Fri" and temp2  > 27) or not swimming2:     #(Yaha equation banega : (False and True) or True  -->  False or True --> True )
    print("Go for swimming.")
else:
    print("Learn Python.")

print("-" * 80)