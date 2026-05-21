# Create a coice based program for below option:
#     Please chhoose your option from below list:
#         1. Learn Python
#         2. Learn Java
#         3. Go Swimming
#         4. Have Dinner
#         5. Go to bed
#         0. Exit 

print("""
Please choose your option from list below:
    1. Learn Pyhton
    2. Lern Java
    3. Go Swimming
    4. Have Dinner
    5. Go to bed
    0. Exit
    """)
choice = 9

while True:
    choice = int(input("Enter your choice option: "))
    if choice in (1,2,3,4,5):
        print("You chose {}". format(choice))
    elif choice == 0:
        print("0")
