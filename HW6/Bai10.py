list_10 = [1, 3, 4, 5, 1, 2, 1, 3, 4, 5, 7, 8, 7, 9, 5, 1, 7]
list_10.sort()
new_list = [1]
count = 1
for i in range(len(list_10)):
    if list_10[i] != new_list[-1]:
        new_list.append(list_10[i])
        count += 1
print(count)