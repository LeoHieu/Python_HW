import random
list_5 = [1, 2, 1, 4, 6, 2, 1, 5, 7, 8, 5, 2, 1, 2]
max_appear = 0
max = []
for i in range(len(list_5)):
    if max_appear < list_5.count(list_5[i]):
        max_appear = list_5.count(list_5[i])
        a = list_5[i]
max.append(a)
for i in range(len(list_5)):
    if max_appear == list_5.count(list_5[i]):
        max.append(list_5[i])
print(f'Phần tử có nhiều lần xuất hiện nhất là: {random.choice(max)}')