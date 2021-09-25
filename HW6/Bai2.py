list_2 = [32, 384, 28, 932, 3213, 485]
max = list_2[0]
min = list_2[0]
for i in range(len(list_2)):
    if max < list_2[i]:
        max = list_2[i]
    if min > list_2[i]:
        min = list_2[i]
print(f'Số lớn nhất trong list là: {max}')
print(f'Số nhỏ nhất trong list là: {min}')