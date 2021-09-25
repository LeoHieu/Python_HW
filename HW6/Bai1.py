list = [2, 1, 5, 8, 9, 4, 6, 1]
sum = 0
multi = 1
for i in range(len(list)):
    sum += list[i]
    multi *= list[i]
print(f'Tổng của các phần tử trong list trên là: {sum}')
print(f'Tích của các phần tử trong list trên là: {multi}')