list_5 = [(1, 2, 5), (0, 0), (9, 13), (14, 8), (5, 5, 9)]
min_a = list_5[0][1]
min = 0
for i in range(len(list_5)):
    if min_a >= list_5[i][1]:
        min_a = list_5[i][1]
        min = i
print(min)
print(list_5[min])