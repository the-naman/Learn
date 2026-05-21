data1 = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

# Data Set for testing:
All_data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
All_data1 = [4, 5, 100, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 200, 350, 360]
start_missing_data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
end_missing_data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
both_missing_data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
out_range_data = [4444, 5444, 1041, 1051, 1101, 1201, 1301, 1301, 1501, 1601, 1701, 1831, 1851, 1871, 1881, 1911, 3501, 3601]
empty_data = []


# Testcases of Outliers:
    # 1. Check if values missing from START.
    # 2. Check if values missing from END.
    # 3. Check if vallues missing from both ENDS.
    # 4. Check if not any range value(any other values) in the list.
    # 5. Check for Empty list


# Code for removing value lower or higher that the min_valid and max_valid:


dataset_list = [All_data,
                All_data1, 
           start_missing_data, 
           end_missing_data,
           both_missing_data, 
           out_range_data, 
           empty_data,
           ]

dataset_name_list = ["All_Data", "All_Data1", "Start Missing Data", "End Missing Data", 
                     "Both Missing Data", "Out Rang Data", "Empty Data"]

valid_choice = []
for i in range(1, len(dataset_name_list)+1):
    valid_choice.append(i)

name = input("Enter your name to proceed: ")
if len(name) > 0:
    print("{}, Welcome Here.".format(name))

choice = None

valid_min = 100
valid_max = 200

min_max_list = []
final_list = []

while len(name) > 0:

    if choice in valid_choice:
        final_dataset = dataset_list[choice-1]
        
        for ds_id, data_val in enumerate(final_dataset):
            if data_val < valid_min:
                min_max_list.append(data_val)

            if data_val > valid_max:
                min_max_list.append(data_val)

        print("")
        print("-"*10, "Final outcome", "-"*20)
        print("Original selected Dataset list: ", final_dataset)
        print("'Valid min = {}', and 'Valid max = {}'.".format(valid_min, valid_max))
        print("List of non-valid items in original list: ", min_max_list)

        for comp_val in final_dataset:
            if comp_val not in min_max_list:
                final_list.append(comp_val)

        print("Final Dataset after removal of non-valid items: ", final_list)
        print("-"*10, "Final outcome", "-"*20)

        break
        
    elif choice == 0:
        print("Successfully Exit")
        break

    else:
        print("Select desired option from below list: ")
        for option_id, option_name in enumerate(dataset_name_list):
            print("{}. {}".format(option_id+1, option_name))
        print("0. Exit")
        
        
        try:
            choice = int(input("Enter your choice for the selection: "))
            
        except ValueError:
            print("Invalid Input")
        
        
    
else:
    print("Invalid input\nPlease Try Again.")


