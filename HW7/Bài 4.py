list_4 = [(5, 3, 7), (1, 9, 5), (8, 4, 1), (1, -1)]
new_list = []
min_i = list_4[0][-1]
min = 0
for i in range(len(list_4)):
    for i in range(len(list_4)):
        if min_i >= list_4[i][-1]:
            min_i = list_4[i][-1]
            min = i
    new_list.append(list_4[i])
    del list_4[i]
    print(list_4)
print(new_list)

