data1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

data = [data1, data2]

odd_num = []
even_num = []

for item in data:
    for num in item:
        if num%2 != 0:
            odd_num.append(num)
        else:
            even_num.append(num)
print("Original Data List: ", data)
print("Odd Number List:    ", odd_num)
print("Even Number List:   ", even_num)
